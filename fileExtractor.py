#!/usr/bin/env python3

from zipfile import ZipFile
import os

choices = ['y','Y','n','N']
noOptions = ['n','N']
filePath = input("What file do you want to unzip:")
customTarget = None
while customTarget not in choices:
    customTarget = input("Do you want to extract these files somewhere other than your current directory? (Y/N):")
if customTarget not in noOptions:
    customTarget = input("What path do you want to extract to?:")
extractOption = None
with ZipFile(filePath, 'r') as zipFile:
    fileNames = zipFile.namelist()
    for fileName in fileNames:
        extractOption = None
        if 'USA' in fileName:
            while extractOption not in choices:
                extractOption = input(f"Do you want to extract {fileName} (Y/N):")
            if extractOption == ("y" or "Y"):
                zipFile.extract(fileName,fileName[:-4])
                with ZipFile(f"{fileName[:-4]}/{fileName}", 'r') as childZip:
                    if customTarget not in noOptions:
                        childZip.extractall(f"{customTarget}/{fileName[:-4]}")
                    else:
                        childZip.extractall(f"{fileName[:-4]}")
                    print(f"Extracting, {fileName}")
                print(f"Deleting file: {fileName[:-4]}")
                os.remove(f"{fileName[:-4]}/{fileName}")