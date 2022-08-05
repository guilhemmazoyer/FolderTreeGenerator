# -*- coding : utf-8 -*-

import sys, time, os

class TreeGenerator:
    output = ""
    depthLevel = 0

    def __init__(self, folderPath):
        self.path = folderPath

    def launch(self):
        if (self.checkFolderExist(self.path)):
            self.readAndExecute(self.path)
            return self.output
        else:
            return 1

    # Verification de l'existence du dossier rentre en parametre
    def checkFolderExist(self, specificPath):
        return os.path.exists(specificPath)

    def isDir(self, pathToFile):
        return os.path.isdir(pathToFile)

    def readAndExecute(self, pathToFolder):
        files = os.listdir(pathToFolder)

        for file in files:
            currentPath = pathToFolder+"\\"+file

            if (self.isDir(currentPath)):
                self.output += ("   " * self.depthLevel) + "\U0001F4C1" + " " + file + '\n'
                self.depthLevel += 1
                self.readAndExecute(currentPath)

            else:
                self.output += ("   " * self.depthLevel) + "\U0001F4C4" + " " + file + '\n'

        self.depthLevel -= 1