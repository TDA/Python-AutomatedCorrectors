import os
import re
__author__ = 'saipc'

def checkForLexer(dirName):
    print "Checks for lexer"
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
        for fileName in files:
            with open(os.path.join(folderName, fileName), 'r') as file:
                data = file.read().replace('\n', '')
                if 'ERROR' in data:
                    print folderName, "error"
                if 'unget' in data:
                    print folderName, "unget"
                matches = re.findall(r"getToken", data)
                count = len(matches)
                if count > 3:
                    print folderName, "get", count


checkForLexer(r"/Users/schandramouli/Documents/CSE 340 Project 2/cse340_f15_p2_submissions/correction-saipc")

def checkForMemoryAlloc(dirName):
    print 'nothing'