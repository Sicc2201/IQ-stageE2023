#########################################################################
"""
Title: CleanupManager.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This file manage and facilitate the cleanup of certain folders

Functions:

- ClearImages(images folder)

- ClearOutput(output folder)

"""
########################################################################

# imports
import os, glob

# delete every file in the images folder (default)
def ClearImages(folder = os.getcwd() + "/" + "Images"):
    filelist = glob.glob(os.path.join(folder, "*")) # get a list of all the content inside the selected folder
    # if content in the folder, delete it
    if filelist:
        print("files to delete:\n")
        for f in filelist:
            print(f + "\n")
        # asks the user confirmation for deleting the files
        while(True):
            keyPressed = input("are you sure you want to delete those files? (y/n):")
            # if yes, delete
            if keyPressed == "y":
                for f in filelist:
                    os.remove(f) 
                break
            # if no, don't delete
            if keyPressed == "n":
                print("clear canceled")
                break
    else:
        print("no files to delete in directory")

# delete every file in the ouput folder (default)
def ClearOutput(folder = os.getcwd() + "/" + "QasmOutput"):
    filelist = glob.glob(os.path.join(folder, "*")) # get a list of all the content inside the selected folder
    # if content in the folder, delete it
    if filelist:
        print("files to delete:\n")
        for f in filelist:
            print(f + "\n")
        # asks the user confirmation for deleting the files
        while(True):
            keyPressed = input("are you sure you want to delete those files? (y/n):")
            # if yes, delete
            if keyPressed == "y":
                for f in filelist:
                    os.remove(f) 
                break
            # if no, don't delete
            if keyPressed == "n":
                print("clear canceled")
                break
    else:
        print("no files to delete in directory")