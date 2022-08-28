'''
instruction:
You are instructed to write a Python code to count and sort, in
descending order, the frequency of words that appeared in a text
file. The list of words' frequency and their count must be stored
in file in a comma-delimited word, freq format.

V1
'''

#!/usr/bin/env python3
import sys

text = open("read.txt","r")
hasil = open("write.txt","w+")

d = dict()
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
	sys.stdout = hasil
	print(key,":",d[key])
