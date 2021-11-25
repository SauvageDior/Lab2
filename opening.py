import sys
import re
import json
import argparse
from tqdm import tqdm
from typing import List

text_file = open('D:\\Labs\\lab2\\10.txt', 'r')
text = text_file.read()

#cleaning
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

#finding unique
unique = []
for line in words:
    if line not in unique:
        unique.append(line)

#sort
unique.sort()

#print
print(unique)