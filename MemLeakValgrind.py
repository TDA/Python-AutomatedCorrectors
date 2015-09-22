__author__ = 'saipc'
import os
import subprocess

def checkFiles(dirName):
    os.chdir(dirName)
    folderList=os.listdir(dirName)
    folderList.pop(0)
    #print folderList
    for folderName in folderList:
        files = os.listdir(folderName)
        if '_test_results_' in files:
            files.remove('_test_results_')
        if 'lexer.c' in files:
            files.remove('lexer.c')
        if 'lexer.h' in files:
            files.remove('lexer.h')
        # this needs a check to see if its a c file or c++ and call the right version of gcc/g++
        #subprocess.call(['gcc', 'project2.c'])

        # theoretically this should work, it worked for the file i compiled myself to a.out
        # now if we can have all the .out files in the dirs, we can simply check for all mem leaks :D
        filePath = os.path.join(dirName, folderName, 'a.out')
        fullFilePathCommand= r"/Users/schandramouli/PycharmProjects/Python_AutomatedCorrectors/script.sh " + filePath
        retVal = subprocess.call('bash ' + fullFilePathCommand, shell=True)
        print retVal
        if retVal == 21:
            print folderName, " has a mem leak "



checkFiles(r"/Users/schandramouli/Documents/CSE_340_Project_2/cse340_f15_p2_submissions/correction-saipc")