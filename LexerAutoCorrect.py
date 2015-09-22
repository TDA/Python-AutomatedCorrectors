import os
import re
__author__ = 'saipc'

def checkForLexer(folderName, fileName):
    #print files
    with open(os.path.join(folderName, fileName), 'r') as file:
        data = file.read().replace('\n', ' ')
        if 'ERROR' in data:
            print folderName, "error"
        if 'unget' in data:
            print folderName, "unget"
        matches = re.findall(r"getToken", data)
        count = len(matches)
        if count > 3:
            print folderName, "get", count

def checkForMemoryAlloc(folderName, fileName):
    with open(os.path.join(folderName, fileName), 'r') as file:
        data = file.read().replace('\n', ' ')
        matches = re.findall(r"(malloc)|(strdup)", data)
        count = len(matches)
        matches2 = re.findall(r"free", data)
        count = count - len(matches2)
        if count != 0:
            print "Checking for proper memory alloc"
            print folderName, fileName, count
            print "---------------------"


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
        for fileName in files:
            checkForLexer(folderName, fileName)
            checkForMemoryAlloc(folderName, fileName)


checkFiles(r"/Users/schandramouli/Documents/CSE_340_Project_2/cse340_f15_p2_submissions/correction-saipc")