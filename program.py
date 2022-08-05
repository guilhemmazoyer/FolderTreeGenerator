# -*- coding : utf-8 -*-

import os, re

class TreeGenerator:
        # Const
    REGEX_CUSTOM_IGNORE_LIST = "[^,]+(?=(,|$))"

        # Params
    maxDepth = 0
    doDefaultIgnoreList = 1
    doCustomIgnoreList = 0

        # Vars
    output = ""
    depthLevel = 0

    defaultIgnoreList = [".git",".vscode","__pycache__"]
    customIgnoreList = []

    def __init__(self, folderPath, depth, doDefault, doCustom):
        self.maxDepth = depth
        self.doDefaultIgnoreList = doDefault
        self.doCustomIgnoreList = doCustom

        self.path = folderPath

    def launch(self, customList):
        if (self.checkFolderExist(self.path)):
            if(self.doCustomIgnoreList):
                #remove spaces
                customList = customList.replace(" ", '')
                #create the list
                self.customIgnoreList = re.split(",", customList, re.MULTILINE)

            self.readAndExecute(self.path)
            return self.output
        else:
            return 1

    # Verification de l'existence du dossier rentre en parametre
    def checkFolderExist(self, specificPath):
        return os.path.exists(specificPath)

    def isDir(self, pathToFile):
        return os.path.isdir(pathToFile)

    def isNotABanWord(self, fileName):
        if (self.doDefaultIgnoreList):
            for name in self.defaultIgnoreList:
                if (fileName == name):
                    return False

        if (self.doCustomIgnoreList):
            for name in self.customIgnoreList:
                if (fileName == name):
                    return False
        
        return True

    def readAndExecute(self, pathToFolder):
        files = os.listdir(pathToFolder)

        for file in files:
            currentPath = pathToFolder+"\\"+file
            if (self.isNotABanWord(file)):
                if (self.isDir(currentPath)):
                    self.output += ("   " * self.depthLevel) + "\U0001F4C1" + " " + file + '\n'
                    self.depthLevel += 1
                    if(self.maxDepth == 0 or self.maxDepth >= self.depthLevel):
                        self.readAndExecute(currentPath)
                    else:
                        self.depthLevel -= 1

                else:
                    self.output += ("   " * self.depthLevel) + "\U0001F4C4" + " " + file + '\n'

        self.depthLevel -= 1