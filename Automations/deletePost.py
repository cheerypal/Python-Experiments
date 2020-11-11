# This file can delete the post link and/or delete the post's .html file
# This file can push to git if the user requires

import sys
import os
import subprocess as cmd
from bs4 import BeautifulSoup as Soup


# This will be called first when the program is executed
def init():
    if len(sys.argv) == 2:
        post = sys.argv[1]
        if post.endswith(".html"):
            print("Finished --->\t\tPost name has been recieved")
            return post
        else:
            print("Error ------>\t\tNo .html file detected")
            exit()
    else:
        print("Error ------>\t\tNo .html file detected")
        exit()


# This will delete the link to the .html file from index.html file
def deleteLink(postName):

    f = open('index.html', "r")
    soup = Soup(f, 'html.parser')

    print("Working ---->\t\tThe link is being deleted")

    remove = soup.find('a', {'id': ''+postName})

    try:
        child = remove.findChildren('div', recursive=True)
    except:
        print("Error ------>\t\tThe link to this .html page does not exist")
        return

    for i in child:
        i.decompose()

    remove.decompose()
    f.close()

    newIndexFile = open('index.html', "w")
    newIndexFile.write(soup.prettify())
    newIndexFile.close()

    print("Finished --->\t\tPost has been deleted from the index.html file")

    return


# This will delete the file from the directory so that the file is completely deleted
def deleteFile(postName):
    check = input("Do you want to delete the post file (y/n)?")
    if check == 'y':
        dir = "C:/Users/euang/Documents/blog.eg.me/posts"
        os.chdir(dir)

        if os.path.isfile(postName):
            print(f"Working ---->\t\tDeleting ./posts/{postName}")
            os.remove(postName)
            print("Finished --->\t\tFile has been deleted")
            return
        else:
            print(f"Error ------>\t\t{postName} does not exist")
            return
    else:
        return


# This will allow the user to push the new repo change to git
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


# Main Method - Sequence of Events
if __name__ == "__main__":
    os.chdir(os.path.abspath(
        "C:/Users/euang/Documents/blog.eg.me/"))
    postName = init()
    deleteLink(postName)
    deleteFile(postName)
    deploy()
    print("\nFinished\n")
