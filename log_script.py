# --encoding: utf-8--
"""
Author: AD OEM team
This script is to process Ottoview logging file,
For more detail, please contact Wentao
"""
import tkinter as tk
from tkinter import filedialog
import os
import time
# import re

# Initialization
path = os.chdir("C:/Users/dj5jgf/Desktop/2017.09.27.14.11.56_ces-sq5-four")
# check 'Wentao_delete_same_error.txt' exists or not
if os.path.exists("WentaoTest.txt"):
    os.remove("WentaoTest.txt")
else:
    print("The file does not exists 1")

# check 'error.txt' exist or not
if os.path.exists('Wentao_delete_same_error.txt'):
    os.remove('Wentao_delete_same_error.txt')
else:
    print("The file does not exists 2")

# Variables declaration
filename1 = []
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilenames()
file_time = (time.ctime(os.stat(file_path[0]).st_ctime))

# Choose file in GUI
for f in file_path:
    fo = f.split('/')
    filename1.append((fo[-1]))
# print(len(filename), filename)
# Print all of file

# index for search
n = 0
m = 0
rb = 0
errors_file = 0
save_file = open("WentaoTest.txt", "w")

# search error message in file content
for file in filename1:
    (filepath, tempfilename) = os.path.split(file)
    (filename, extension) = os.path.splitext(tempfilename)
    if extension == "":
        n = n + 1
        errorfile = "Error" + filename
        # print("Useful files: %d" % n, file)
        with open(file) as f:
            errorfile = []
            content = f.readlines()
            """
            # if "ERROR" in content:
            #     errors_file = errors_file + 1
            #     print(errors_file)
            """
            # Find error txt
            content = [x.strip() for x in content]
            for lines in content:
                # print(lines)
                if "ERROR" in lines:
                    errorfile.append(lines)
                    feature = lines.split()[5]
                    # print(str(lines.split()[6:-1]))
                    save_file.write(str(file) + "," + str(lines.split()[7:-1]) + "," + "\n")
                else:
                    pass
            save_file.write(str(file) + " " +"=====================  New file    ====================" + "\n")

    else:
        m = m + 1
        if extension == ".rb":
            rb = rb + 1
        # for debugging
        # print("Useless files: %d" % m, file)

# close opening file
save_file.close()
f.close()
# count error message file
for file in filename1:
    (filepath, tempfilename) = os.path.split(file)
    (filename, extension) = os.path.splitext(tempfilename)
    if extension == "":
        with open(file) as g:
            errorfile = []
            word = g.read().split(' ')
            if "ERROR" in word:
                errors_file = errors_file + 1
            else:
                pass
g.close

# process previous output file
rFile = open('WentaoTest.txt', 'r')
wFile = open('Wentao_delete_same_error.txt', 'w')
allLine = rFile.readlines()
rFile.close()
s = set()
for ii in allLine:
    s.add(ii)
for i in s:
    wFile.write(i)
wFile.close()

# for debugging
# open('Wentao_delete_same_error.txt', 'w').write(''.join(set(open('WentaoTest.txt').readlines())))

# Summary
print("Logging time:", file_time)
print("All log files :", len(filename1))
print("Ruby files : ", rb)
print("Useless files : ", m)
print("Readable files:", n)
print("Errors files:", errors_file)
print("Done")

# write any header you want to the final file
with open('Wentao_delete_same_error.txt', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write("Logging time:" + file_time + '\n' + "All log files :" + len(filename1) + "\n" + "Ruby files : " + rb\
            + "\n" + "Useless files : " + m + "\n" + "Readable files:" + n + "Errors files:" + errors_file + "\n" + content)
# Process file begins
# todo: Check with Tonmoy and Bob for more detail

