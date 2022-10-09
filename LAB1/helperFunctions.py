import time
import os
import math
import numpy as np
import glob
from sys import getsizeof
import random
from constants import MB

def inputSize():
    filename = str(input("Enter your filename: "))
    size = int(input("Enter the size in MB: "))
    amountOfAdditionalFiles = 8 + int(math.log2(size)) if math.log2(size) > 0 else 5
    return filename, size, amountOfAdditionalFiles


def writeToFile(currentList, file, appendNewline=False):
    newline = "\n"
    textCurrentList = ""
    if appendNewline:
        file.write(newline)
        return
    if type(currentList) == list:
        for number in currentList:
            textCurrentList += str(number) + newline
        file.write(textCurrentList + newline)
    else:
        file.write(str(currentList) + newline)

def generateNumbers(fileName, size):
    print("Starting the generation of file...\n")

    start = time.process_time()
    with open(fileName, 'wb') as fout:
        fout.write(os.urandom(size*MB))
    end = time.process_time()
    print("Generation succeeded!")
    return end-start

def txtGenerator(fileName, size):
    start = time.process_time()
    generateNumbers("test.bin", size)
    f = open("test.bin", 'r')
    a = np.fromfile(f, dtype=np.uint32)
    with open(fileName, 'w') as fout:
        for num in a:
            fout.write(str(num) + '\n')
    end = time.process_time()
    return (end-start)

def delete_dir(path):
    files = glob.glob(path)
    for f in files:
        os.remove(f)

def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# function to perform quicksort


def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

