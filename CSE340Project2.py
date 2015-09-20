import os
import shutil
__author__ = 'saipc'

def separateFilesToBeCorrected(dirName):
    # do nothing now
    os.chdir(dirName)
    folders = []
    correctionList = r"/Users/schandramouli/Documents/correctionList"
    with open(correctionList) as file:
            folders = file.readlines()
    print folders

    folderList=os.listdir(dirName)
    for folderName in folderList:
        formattedFolderName = str(folderName) + "\n"
        if formattedFolderName in folders:
            print folderName
            copyDirectory(folderName, os.path.join(dirName, r"correction-saipc", folderName))

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


separateFilesToBeCorrected(r"/Users/schandramouli/Documents/CSE 340 Project 2/cse340_f15_p2_submissions")
