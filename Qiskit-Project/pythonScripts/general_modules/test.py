import os, glob

def ClearImages(folder = os.getcwd() + "/images"):
    filelist = glob.glob(os.path.join(folder, "*"))
    if filelist:
        print("files to delete:\n")
        for f in filelist:
            print(f + "\n")
        while(True):
            keyPressed = input("are you sure you want to delete those files? (y/n):")
            if keyPressed == "y":
                print("files deleted")
                break
            if keyPressed == "n":
                print("clear canceled")
                break
    else:
        print("no files in directory")
ClearImages()