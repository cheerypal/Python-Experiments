# This will take a post that is stored in a .md file and post it as a new html file.
# This will also push to git repo when the post has been updated or created if the user wants of course
# @author : Euan Gordon

import sys
import os
import markdown
import subprocess as cmd
from datetime import date
from bs4 import BeautifulSoup as Soup


def init():
    # Get the file from the command line
    # Check if the file is a .md file and check if the file exists before continuing
    if len(sys.argv) == 2:
        file = sys.argv[1]
        if file.endswith(".md"):
            if os.path.isfile(file):
                print("Finished --->\t\tFile Found")
                return file
            else:
                print("Error ------>\t\tThe file does not exist")
        else:
            print("Error ------>\t\tNo .md file detected")
        exit()
    else:
        print("Error ------>\t\tNo .md file detected")
        exit()


# This will look through the .md file and will update a current file or create a new one
def lookThough(file):
    # Open up the .md file and and get the name for the new html file that will be created.
    dir = "C:/Users/euang/Documents/blog.eg.me/posts"
    newFile = False
    fileName = file.replace(".md", "")
    fileTitle = fileName
    fileName = fileName + ".html"

    f = open(file, "r")
    print("Working ---->\t\tReading .md File")

    # Create the boiler plate for the new post.html file
    boilerplate = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./posts.css" />
    <link rel="stylesheet" href="../assets/index.css" />
    <link rel="icon" href="../assets/logo.png" />
    <title>Post</title>
  </head>
  <body>
    <div class="post">
"""

    # Convert the markdown file to html using Python Markdown
    post = markdown.markdown(
        f.read(), extensions=['attr_list', "md_in_html"])

    footer = """ 
    </div>
  </body>
</html>
"""

    # Create the htmlfile
    htmlFile = boilerplate + post + footer
    f.close()

    os.chdir(dir)

    # Check if the html file already exists
    if os.path.isfile(fileName):
        newFile = False
        print("Working ---->\t\tUpdating File")
    else:
        newFile = True
        print("Working ---->\t\tCreating New File")

    newPost = open(fileName, "w")
    newPost.write(htmlFile)

    newPost.close()

    print("Finished --->\t\tPost Generated")

    return fileTitle, fileName, newFile


# This will add a new link to the new blog post if the post has not already been pushed to the blog
def addToIndex(title, file):
    # Changes dir to the main dir
    dir = "C:/Users/euang/Documents/blog.eg.me"
    os.chdir(dir)

    # Gets the date for the post
    today = date.today()
    today = '' + today.strftime('%d/%m/%Y')

    # HTML Boilerplate for the link to the new post
    html = """ 
    <a id='"""+file+"""' href="./posts/""" + file + """">
        <div>
          <span class="title-link">""" + title + """</span>
          <span class="date">""" + today + """</span>
        </div>
      </a>"""

    # Opens the main blog page creates a soup of the file and adds the new post link to after the <b></b> tag
    f = open("index.html", "r")
    soup = Soup(f, "html.parser")
    title = soup.find('b')
    post = Soup(html, "html.parser")
    title.insert_after(post)
    print("Finished --->\t\tindex.html has been updated")
    f.close()

    # Rewrites the file with the post added to the html
    newFile = open('index.html', "w")
    newFile.write(soup.prettify())
    newFile.close()

    print("Finished --->\t\tNew post created and has been added to the blog")


# This will deploy the new blog post to github
def deploy():
    check = input("Do you want to commit to github (y/n)?")
    if check == "y":
        commitmsg = input("Commit msg:\n")
        os.chdir(os.path.abspath("C:/Users/euang/Documents/blog.eg.me"))
        cp = cmd.run("git add .", check=True, shell=True)
        print("git add .")
        cp = cmd.run(f"git commit -m {commitmsg}", check=True, shell=True)
        print(f"git commit -m {commitmsg}")
        cp = cmd.run("git push", check=True, shell=True)
        print("git push")
    else:
        return


if __name__ == '__main__':
    os.chdir(os.path.abspath(
        "C:/Users/euang/Documents/blog.eg.me/posts/new_posts"))
    # Triggers the initial function to get the file that we are going to convert to a blog post.
    file = init()

    # Gets the title, filename and check for if the file is a new file after creating the blog post html page
    title, name, newFile = lookThough(file)

    # This will trigger the addToIndex function to add the link to the index.html page - only if the file is a newFile
    # This will ask the user if they want to commit to github

    if newFile == True:
        addToIndex(title, name)
        deploy()
        print("\nFinished\n")
        exit()
    else:
        print("Finished --->\t\tThe post has been updated")
        deploy()
        print("\nFinished\n")
