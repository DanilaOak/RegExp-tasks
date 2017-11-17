#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
1 Stemmer
a) Create a program that reads the existing text file verbs. txt with one English verb per line and then uses regular
expressions to separate the trunk from the verb for each word. Irregular verbs should also be intercepted.
Exceptions are to be looked up in a Dictionary. For this task you can use the enclosed code skeleton task1.py.
The output is done on the terminal and could look like this:
listens -> listen s
     panicking -> panic k ing
     followed -> follow ed
     claim -> claim
b) Extend your program from a) so that the user can select via program call whether an entire text file or a string
is to be lemmatized.
• 1. Option:           $ python stemmer.py data.txt
 • 2. Option           $ python stemmer.py "stemming"
"""
import re, sys

# Dictionary of irregular verbs
irregulars = {"mimick": "mimic", "reli": "rely", "withheld": "withhold", "locat": "locate"}

# Read in arguments

# Your code

# Read the verbs into a list
verb_list = []

# Your code

# Iterate through list, and check with regex
for verb in verb_list:
    print("Stemming...") #Dummy Zeile

    # Your code