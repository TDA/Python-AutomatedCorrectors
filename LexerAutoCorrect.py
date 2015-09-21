import os
import re
__author__ = 'saipc'

def checkForLexer(dirName):
    os.chdir(dirName)
    folderList=os.listdir(dirName)
    folderList.pop(0)
    errorRE = re.compile(r"ERROR")
    ungetTokenRE = re.compile(r"ungetToken\(\)")
    #print folderList
    for folderName in folderList:
        files = os.listdir(folderName)
        if '_test_results_' in files:
            files.remove('_test_results_')
        if 'lexer.c' in files:
            files.remove('lexer.c')
        if 'lexer.h' in files:
            files.remove('lexer.h')
        #print files
        if len(files) == 1:
            with open(os.path.join(folderName, files.pop()), 'r') as file:
                data = file.read().replace('\n', '')
                if 'ERROR' in data:
                    print folderName, "error"
                if 'unget' in data:
                    print folderName, "unget"



checkForLexer(r"/Users/schandramouli/Documents/CSE 340 Project 2/cse340_f15_p2_submissions/correction-saipc")