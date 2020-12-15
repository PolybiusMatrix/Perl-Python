#!/bin/env python3.5

#This will allow you to find any directory in the ENTIRE computer system
#argv[1] = directory you want to find - Code will build the absolute path for you to use
#argv[2] = the file extension you are looking to replace (THIS WILL CHANGE EXTENSION OF ALL MATCHING FILES)
        #If you don't want to change file extentions then adjust argv[2] and argv[3] as you like
#argv[3] = the file extension you are replacing the old one with
import os
import sys
if(len(sys.argv) != 4):
    print('Usage: ', sys.argv[0], 'filename')
    sys.exit(1)

oldExt = sys.argv[2]
newExt = sys.argv[3]

reqDir = sys.argv[1]
dirList = [os.getcwd()]
path = dirList[0]
while os.path.abspath(os.path.join(path, os.pardir)) != '/':
        path = os.path.abspath(os.path.join(path, os.pardir))
        dirList.append(path)
dirList.append(os.path.abspath(os.path.join(path, os.pardir)))

dirList.reverse()
print(dirList)

while len(dirList) > 0:
        curr_path = dirList.pop()
        parent_path = os.path.abspath(os.path.join(curr_path, os.pardir))

        if os.path.join(parent_path, reqDir) == curr_path:

                break
        paths = [str(curr_path + "/" + i) for i in os.listdir(curr_path) if os.path.isdir(curr_path + "/" + i)]
        #print("Current Path: ", curr_path)
        dirList.extend(paths)

print(curr_path)
#BEYOND THIS IS WHERE YOU CAN IMPLEMENT WHATEVER CODE YOU WANT TO DO WHATEVER SERVICE YOU'D LIKE
#print(os.listdir(curr_path))
for file in os.listdir(curr_path):
   if(file.endswith(sys.argv[2])):
        print(file)
        filename = file[:-len(sys.argv[2])] #filename consists of everything BUT the extension
        filename = filename + sys.argv[3]   #change the extension for print purposes
        print(filename) #see current change
        oldPath = curr_path + '/' + file
        newPath = curr_path + '/' + filename
        os.rename(oldPath, newPath)
#os.rename(r'curr_path\*.argv[2]', r'curr_path\*.argv[3]')

#Quite literally stores every single directory/subdirectory/file/ANYTHING in this list
#Had to make sure
#dirlist = [(root, dirs, files) for root, dirs, files in os.walk("/Users/mitchellgeer")]
