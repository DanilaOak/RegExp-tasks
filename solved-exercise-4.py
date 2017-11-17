#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import re

# Collect the command line arguments
try:
    name = sys.argv[1]
# If not command line arguments use default file
except IndexError:
    name = 'yearbook.txt'

# Saving the file in a data structure
with open(name, 'r', encoding='utf-8') as jahrbuch:
    words = []
    for line in jahrbuch:
        line = re.sub(r'\t', ' ', line)
        words.append(line.rstrip())


print("\n------------------- \n"
      "Wörter mit -ier-, welche mit demselben Buchstaben beginnen und enden, und ihre POS-Tags\n")
found_ier = []
pattern = re.compile(r'([a-z])\w*ier\w*\1 \w*')
for item in words:
    if pattern.search(item):
        found_ier.append(pattern.search(item).group())


found_ier_unique = set(found_ier)
for found in found_ier_unique:
    print(found)

matt = []
pattern = re.compile(r'\w*Matterhorn\w*')
word = re.compile(r'^\w*.')
print("\n------------------- \nKontext von Matterhorn\n")
for i in range(0, len(words)):
    if pattern.search(words[i]):
        print(word.search(words[i - 2]).group(),
              word.search(words[i - 1]).group(),
              word.search(words[i]).group(),
              word.search(words[i + 1]).group(),
              word.search(words[i + 2]).group())
