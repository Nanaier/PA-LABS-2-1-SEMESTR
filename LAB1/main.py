from helperFunctions import inputSize, generateNumbers, delete_dir
from MultiwayMerge import separatingByFiles, merge_files
from optimization import merge_files_optimize, divide_input_file
import time, os
from constants import path, path_to_folder, MAX_SIZE_OF_CHUNK


fileName, size, amountFiles, sortType = inputSize()
tm = generateNumbers(fileName, size)

print("Time spent(in seconds) on generations: ", tm)
if sortType == "n":
    print("Sorting starts...")
    separatingByFiles(fileName, amountFiles, size)
    start = time.time()
    namesOfFiles = merge_files([str(i) for i in range(amountFiles)])
    flag = 'B'
    while len(namesOfFiles) > 1:
        flag = 'C' if flag == 'B' else 'B'
        namesOfFiles = merge_files(namesOfFiles)
    flag = 'C' if flag == 'B' else 'B'
    os.rename(path + flag + str(namesOfFiles[0]) + ".txt", "Result.txt")
    delete_dir(path_to_folder)
    end = time.time()
    print("\nSorting ended, you can check your result file")
    print("Time spent on sorting: ", str(end - start), "seconds")
if sortType == "o":
    print("Sorting starts...")
    start = time.time()
    namesOfFiles = divide_input_file(fileName, MAX_SIZE_OF_CHUNK)
    merge_files_optimize(namesOfFiles)
    end = time.time()
    print("\nSorting ended, you can check your result file")
    print("Time taken: ", str(end - start), "seconds / ", str((end - start) / 60), "minutes")


# 'output_filename.bin'
