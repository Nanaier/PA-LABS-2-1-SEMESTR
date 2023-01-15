import os
import math
import time
from helperFunctions import writeToFile
import numpy as np
from constants import path, MB
from os.path import exists


def separatingByFiles(fileName, amountOfFiles, size):
    try:
        os.remove("Result.txt")
    except FileNotFoundError:
        pass
    filesB = []
    for file in range(amountOfFiles):
        filesB.append(open(path + "B" +str(file) + ".txt", "w"))
    currentList = []
    currentIndex = 0
    currentFile = 0

    byteSize = os.path.getsize(fileName)
    amn = math.floor(byteSize/(10*MB))
    left_amn = byteSize - (10*MB)*amn
    
    for i in range(0, amn):
        a = np.fromfile(fileName, count=int(10 * MB / 4), offset=i*10*MB, dtype=np.uint32)
        for number in a:
            if currentIndex != 0 and currentList[currentIndex - 1] >= number:
                writeToFile(currentList, filesB[currentFile % amountOfFiles])
                currentFile += 1
                currentIndex = 0
                currentList.clear()
            currentIndex += 1
            currentList.append(number)

    writeToFile(currentList, filesB[currentFile % amountOfFiles])
    a = np.fromfile(fileName, count=int(left_amn/ 4), offset=amn*10*MB, dtype=np.uint32)
    for number in a:
        if currentIndex != 0 and currentList[currentIndex - 1] >= number:
            writeToFile(currentList, filesB[currentFile % amountOfFiles])
            currentFile += 1
            currentIndex = 0
            currentList.clear()
        currentIndex += 1
        currentList.append(number)
    writeToFile(currentList, filesB[currentFile % amountOfFiles])
    for file in filesB:
        file.close()
    print("Initial file separated successfully!")


def merge_files(fileNames):

    amountOfFiles = len(fileNames)
    currentList = []
    writeFiles = []
    readFiles = []
    fileSizes = [0] * amountOfFiles
    newSerialFileNames = []
    currentCFiles = 0
    amountOfFilesAfterMerge = amountOfFiles

    print("\nNew phase of merging started...")
    for i, name in enumerate(fileNames):
        if exists(path + "B" + name + ".txt"):
            fileSizes[i] = os.path.getsize(path + "B" + fileNames[i] + ".txt")
            writeFiles.append(open(path + "C" + name + ".txt", "w"))
            readFiles.append(open(path + "B" + name + ".txt", "r"))
        else:
            fileSizes[i] = os.path.getsize(path + "C" + fileNames[i] + ".txt")
            writeFiles.append(open(path + "B" + name + ".txt", "w"))
            readFiles.append(open(path + "C" + name + ".txt", "r"))

        symbol = readFiles[i].readline()
        fileSizes[i] -= len(symbol) + 1
        if symbol != "\n" and symbol != "":
            currentList.append(int(symbol))
        else:
            fileSizes[i] = 0
            currentList.append(float('inf'))
            amountOfFilesAfterMerge -= 1
    while any(x > 1 for x in fileSizes):
        while amountOfFilesAfterMerge > 0 and len(currentList)<10000000:
            min_element = min(currentList)
            min_index = currentList.index(min_element)
            writeToFile(min_element, writeFiles[currentCFiles % amountOfFiles])
            currentList.pop(min_index)
            symbol = readFiles[min_index].readline()
            fileSizes[min_index] -= len(symbol) + 1
            if symbol != "\n" and symbol != "":
                currentList.insert(min_index, int(symbol))
            else:
                currentList.insert(min_index, float('inf'))
                amountOfFilesAfterMerge -= 1
        writeToFile(None, writeFiles[currentCFiles % amountOfFiles], True)
        currentCFiles += 1
        currentList.clear()
        amountOfFilesAfterMerge = amountOfFiles
        for i in range(amountOfFiles):
            symbol = readFiles[i].readline()
            fileSizes[i] -= len(symbol) + 1
            if symbol != "\n" and symbol != "":
                currentList.append(int(symbol))
            else:
                fileSizes[i] = 0
                currentList.append(float('inf'))
                amountOfFilesAfterMerge -= 1
    for file in writeFiles:
        file.close()
    for i, file in enumerate(readFiles):
        if currentCFiles - 1 >= i:
            newSerialFileNames.append(str(int((file.name[:-4])[35:])))
        file.close()
        os.remove(file.name)
    print("Files merged(one of the multiple merges)...")
    return newSerialFileNames
