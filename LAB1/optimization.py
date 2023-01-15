import math
import os
import time

import numpy as np

from LAB1.constants import MB
from helperFunctions import writeToFile

def divide_input_file(fileName, chunk):
    try:
        os.remove("Result.txt")
    except FileNotFoundError:
        pass

    currentFile = 0

    byteSize = os.path.getsize(fileName)
    amn = math.floor(byteSize / (10 * MB))
    left_amn = byteSize - (10 * MB) * amn

    for i in range(0, amn):
        a = np.fromfile(fileName, count=chunk, offset=i * chunk * 4, dtype=np.uint32)
        with open(f"{currentFile}.txt", "w") as numbers_to_file:
            a.sort()
            for number in a:
                writeToFile(number, numbers_to_file)
            currentFile += 1
            print("Created file number:", currentFile)
    a = np.fromfile(fileName, count=int(left_amn / 4), offset=amn * chunk * 4, dtype=np.uint32)
    with open(f"{currentFile}.txt", "w") as numbers_to_file:
        a.sort()
        for number in a:
            writeToFile(number, numbers_to_file)
        currentFile += 1
        print("Created file number:", currentFile)
    return [f"{i}" for i in range(currentFile)]


def merge_files_optimize(previous_names):
    """function for merging small series into larger series"""
    print("Merging started")
    num_of_files = len(previous_names)
    output_file = open("Result.txt", "w")
    curr_elements = []
    file_handler = []
    real_length = num_of_files
    for i, name in enumerate(previous_names):
        # opening files
        file_handler.append(open(name + ".txt", "r"))
        symbol = file_handler[i].readline()
        # reading the first characters of each file and adding them to the list
        if symbol != "\n" and symbol != "":
            curr_elements.append(int(symbol))
        else:  # if the file runs out of numbers, decrease the number of files with characters
            curr_elements.append(float('inf'))
            real_length -= 1
    while real_length > 0:  # internal loop that works as long as at least one file contains numbers related to the current series
        min_element = min(curr_elements)
        min_index = curr_elements.index(min_element)
        # writing the smallest number from the list of first numbers in each file to the output file
        writeToFile(min_element, output_file)
        curr_elements.pop(min_index)
        # replacing this number with the next one from the same file
        symbol = file_handler[min_index].readline()
        if symbol != "\n" and symbol != "":
            curr_elements.insert(min_index, int(symbol))
        else:
            curr_elements.insert(min_index, float('inf'))
            real_length -= 1
    writeToFile(None, output_file, True)
    curr_elements.clear()
    real_length = num_of_files
    # repeating the procedure for the next series
    for i in range(num_of_files):
        symbol = file_handler[i].readline()
        if symbol != "\n" and symbol != "":
            curr_elements.append(int(symbol))
        else:
            curr_elements.append(float('inf'))
            real_length -= 1
    output_file.close()
    for file in file_handler:
        file.close()
        os.remove(file.name)


