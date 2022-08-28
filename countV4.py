'''
instruction:
You are instructed to write a Python code to count and sort, in
descending order, the frequency of words that appeared in a text
file. The list of words' frequency and their count must be stored
in file in a comma-delimited word, freq format.
'''

#!/usr/bin/env python3
import string
text = open("sample2.txt", "r")
hitung = dict()

for line in text:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ")
    for word in words:
        if word in hitung:
            hitung[word] = hitung[word] + 1
        else:
            hitung[word] = 1

for key in list(hitung.keys()):
    print(key, " ", hitung[key])

