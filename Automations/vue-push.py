import subprocess as cmd
import sys
import os

# Created to improve pushing a vue application to a heroku git repository and/or to a github repo
# This can also trigger the linting of vue code if you have a linter available


def main():

    lint = False
    heroku = False

    # Get and check for arguments

    for i in range(len(sys.argv)):

        if sys.argv[i] == "-l" or sys.argv[i] == "lint":
            lint = True

        if sys.argv[i] == "-h" or sys.argv[i] == "heroku":
            heroku = True

    # Commit msg for git
    commitMsg = input("Type your commit msg here:\n")

    # Check if their is a request to lint or push to heroku
    if lint == True or heroku == True:
        os.chdir(os.path.abspath("path of vue application"))
        if lint == True:
            cp = cmd.run("npm run lint", check=True, shell=True)
            print(cp)
        if heroku == True:
            cp = cmd.run('npm run build', check=True, shell=True)
            print(cp)

    # Push to GitHub
    os.chdir(os.path.abspath("path git directory"))
    cp = cmd.run("git add .", check=True, shell=True)
    print(cp)
    cp = cmd.run(f"git commit -m '{commitMsg}'", check=True, shell=True)
    print(cp)
    cp = cmd.run("git push", check=True, shell=True)
    print(cp)

    # Push to heroku if requested
    if heroku == True:
        cp = cmd.run(
            "git subtree --prefix {name-of-vue-application} push heroku master", check=True, shell=True)
        print(cp)


if __name__ == '__main__':
    main()
