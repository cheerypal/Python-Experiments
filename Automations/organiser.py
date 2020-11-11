# This is an automated python script that will move, sort and organise files in a directory of choice
# @author Euan Gordon

import sys
import os
import glob
import shutil
import subprocess as cmd
import pathlib

documentsCd = "C:/Users/euang/Documents"
downloads = "C:/Users/euang/Downloads"
pictures = "C:/Users/euang/Pictures"


def init():
    images = False
    documents = False
    currentFolder = ""
    destinationFolder = ""
    sort = False

    # Arguments section for the script
    if sys.argv[1] == "-img" or sys.argv[1] == "-i":
        images = True
        print("Initialize -->\tImages Selected")
    elif sys.argv[1] == "-doc" or sys.argv[1] == "-d":
        documents = True
        print("Initialize -->\tDocument Selected")
    elif sys.argv[1] == "-help" or sys.argv[1] == "-h":
        print("-img -i\t\t\tThis will move and/or organise images")
        print("-doc -d\t\t\tThis will move and/or organise documents")
        print("-all -a\t\t\tThis will sort everything images and documents")
        print("-help -h\t\tThis will bring up the help txt")
        print("-sort -s\t\tThis will organise files by file type")
        print("-nosort -ns\t\tThis will stop sorting\n\n")
        print("Example:\n")
        print(
            "python3 organiser <[-img, -doc, -all, -help]> <[-sort, -nosort]> <current_path> <destination_path(optional)>\n\n")

        exit()

    elif sys.argv[1] == "-all" or sys.argv[1] == "-a":
        images = True
        documents = True
        print("Initialize -->\tAll Files Selected")

    if sys.argv[2] == "-sort" or sys.argv[2] == "-s":
        sort = True
        print("Initialize -->\tSort By File Type Selected")
    elif sys.argv[2] == "-nosort" or sys.argv[2] == "-ns":
        sort = False
        print("Initialize -->\tNo Sort Selected")

    if len(sys.argv) > 3:
        if sys.argv[3] == "documents":
            print("Initialize -->\tFolder Found\n")
            currentFolder = documentsCd
            destinationFolder = documentsCd

        elif sys.argv[3] == "pictures":
            print("Initialize -->\tFolder Found\n")
            currentFolder = pictures
            destinationFolder = pictures

        elif sys.argv[3] == "downloads":
            print("Initialize -->\tFolder Found\n")
            currentFolder = downloads
            destinationFolder = downloads

        elif os.path.isdir(sys.argv[3]):
            print("Initialize -->\tFolder Found\n")
            currentFolder = sys.argv[3]
            destinationFolder = sys.argv[3]
        else:
            print("Initialize -->\tFolder Not Found\n")

    else:
        print("Initialize -->\tNo path was given\n")

    if len(sys.argv) > 4:
        if sys.argv[4] == "documents":
            print("Initialize -->\tDestination Folder Found\n")
            destinationFolder = documentsCd

        elif sys.argv[4] == "pictures":
            print("Initialize -->\tDestination Folder Found\n")
            destinationFolder = pictures

        elif sys.argv[4] == "downloads":
            print("Initialize -->\tDestination Folder Found\n")
            destinationFolder = downloads

        elif os.path.isdir(sys.argv[4]):
            print("Initialize -->\tDestination Folder Found\n")
            destinationFolder = sys.argv[4]
        else:
            print("Initialize -->\tFolder Not Found")
            print("Initialize -->\tCreating Folder")
            destinationFolder = sys.argv[4]
            os.mkdir(f"{destinationFolder}")

    else:
        print("Initialize -->\tFolder Not Found")

    return images, documents, currentFolder, destinationFolder, sort


# Will organise and sort file from a specific folder
def organise(curr, dest, sort, fileTypes, folderName):
    files = []

    os.chdir(curr)

    for file in fileTypes:
        files.extend(glob.glob(file))

    if sort == True:
        for f in range(len(folderName)):
            print(f"Working ----->\tSearching for -> {dest}/{folderName[f]}")
            if os.path.isdir(f"{dest}/{folderName[f]}"):
                print(f"Found ------->\t{dest}/{folderName[f]}\n")
                continue
            else:
                print(f"Working ----->\tCreating -> {dest}/{folderName[f]}\n")
                os.mkdir(f"{dest}/{folderName[f]}")

    for f in range(len(files)):
        if sort == True:
            for i in range(len(folderName)):
                if files[f].endswith(folderName[i]):
                    print(
                        f"Working ----->\tMoving '{files[f]}' to '{dest}/{folderName[i]}'\n")
                    shutil.move(
                        f"{curr}/{files[f]}", f"{dest}/{folderName[i]}/{files[f]}")
                    break
        else:
            print(f"Working ----->\tMoving {files[f]} to {dest}")
            shutil.move(
                f"{curr}/{files[f]}", f"{dest}/{files[f]}")

    print("***** Finished *****")


# start
if __name__ == '__main__':
    img, doc, curr, dest, sort = init()
    if img == True:
        types = ("*.heic", "*.png", "*.jpg", "*.gif", "*.jpeg", "*.svg", "*.uxf")
        folderNames = ["heic", "png", "jpg", "gif", "jpeg",
                       "svg", "uxf", "PNG", "JPG", "JPEG", "GIF", "SVG", "UXF", "HEIC"]
        print("Organising -->\tImages......\n")
        organise(curr, dest, sort, types, folderNames)

    if doc == True:
        types = ("*.pdf", "*.doc", "*.docx",
                 "*.txt", "*.rtf", "*.xls", "*.xlsx", "*.tmp")
        folderNames = ["pdf", "doc", "docx", "xls",
                       "xlsx", "tmp", "PDF", "DOC", "DOCX", "XLS", "XLSX", "TMP"]
        print("Organising -->\tDocuments......\n")
        organise(curr, dest, sort, types, folderNames)
