#!/usr/bin/env python3
count = 0
f = open("sample.txt", "r")
for line in f:
    word = line.split(" ")
    count += len(word)
print("Total Number of Words: " + str(count))
f.close()
