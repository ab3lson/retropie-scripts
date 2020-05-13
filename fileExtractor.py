#!/usr/bin/env python3

from zipfile import ZipFile

choices = ['y','Y','n','N']
filePath = input("What file do you want to extract:")
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
                    childZip.extractall(f"{fileName[:-4]}")
                    print(f"Extracting, {fileName}")

