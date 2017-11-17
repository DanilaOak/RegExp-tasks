#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4 Search books with Python
In the first exercise, you searched through yearbooks from Corpus with the help of command police tools such as grep,
wc etc. In this exercise, you should do the same with Python and the Python module re. Write a program that accepts
a yearbook.txt as an argument and does the following:
save the yearbook in utf-8
The POS tag and the lemma should be retrievable from each token.

The output in the terminal:

which words begin and end with the same letter and contain -ier- be- in addition. What are their POS?

sentiers N_C
Steiermärkers NN
Tierlaut NN
Eisbarriere NN
...

between which four tokens the proper name Matterhorn occurs:
...schlimm . Matterhorn , Weisshorn...
...will aufs Matterhorn . Aber...
...wird das Matterhorn besteigen ,...
...
"""
import sys, re

# Collect the command line arguments
name = sys.argv[1]

# Saving the file in a data structure
with open(name,'r', encoding='utf-8') as jahrbuch:
	words = []
	for line in jahrbuch:
        # Yourcode

#Looking for tokens with -ier- in them which begin and end with the same vocal
print("\n------------------- \nWörter mit -ier-, welche mit demselben Buchstaben beginnen und enden, und ihre POS-Tags\n")
found_ier = []

# Your code

found_ier_unique = set(found_ier)
for found in found_ier_unique:
    print(found) # Dummy line

    # Your code



# Looking for the context of the German noun Berg
print("\n------------------- \nKontext von Matterhorn\n")
for i in range(0,len(words)):
    print("...Matterhorn...") # Dummy line

    # Your code

