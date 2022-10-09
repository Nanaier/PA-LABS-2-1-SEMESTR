from helperFunctions import inputSize, generateNumbers, delete_dir
from MultiwayMerge import separatingByFiles, merge_files
import time, os
from constants import path, path_to_folder


fileName, size, amountFiles = inputSize()
tm = generateNumbers(fileName, size)
print("Time spent(in seconds) on generations: ", tm)

print("Sorting starts...")
separatingByFiles(fileName, amountFiles)
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


# 'output_filename.bin'
