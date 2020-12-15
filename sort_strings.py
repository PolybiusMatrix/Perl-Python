#!/bin/env python3
import sys

fileLines = []
#Check to make sure the user input a filename on the command line
if(len(sys.argv) != 2):
    print('Usage: ', sys.argv[0], 'filename')
    sys.exit(1)

file = open(sys.argv[1])
#Load each word into an array
for line in file:
    fileLines.append(line)

store = dict()

for word in fileLines:
    vowOnly = ''
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for char in word:
        if char in vowels:
            vowOnly += char

    store[word] = vowOnly

answer = sorted(store.keys(), key=lambda x: store[x])
for x in answer:
    print(x)
# create dict (word -> word_vowels)
# sort dictionary keys by value sorted(dict.keys(), key=lambda x: dict[x])

file.close()
