#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
3 Comparing texts
To deepen your knowledge of dictionaries, you will create a program in this exercise that efficiently
examines two texts. The texts are to be included in the program call:
$ python task1.py text1.txt text2.txt
a) Which words appear in both files? The program should output the common words with their respective
frequencies per text. Output proposal:
words in common:

     going –– text1: 1 text2: 1
     away –– text1: 1 text2: 1
     unknown –– text1: 1 text2: 1
     ...
     . –– text1: 18 text2: 19
     the –– text1: 36 text2: 18
     , –– text1: 36 text2: 40
 
b) Extend a) so that the user can select via program call whether the output should be sorted alphabetically
 or by absolute frequency (i. e. occurrences in both texts combined):
$ python task3.py text1.txt text2.txt --alpha
     $ python task3.py text1.txt text2.txt  --freq
 
b) Additional task: Customize your program so that it can compare more than two files.
$ python task3.py text1.txt text2.txt text3.txt --freq  
You are welcome to use the two tokenized texts in the exercise folder for this task. For this exercise the code
skeleton task3.py is available, which can give you an orientation when programming.
Name your program as described above.
"""
import sys, re

# Collect the command line arguments

texts = sys.argv[1:]
option = False

# Create dictionaries of texts' words and put them into a list
dictionaries = []
for data in texts:
    words = {}

    # Your code

    dictionaries.append(words)

# Looking for words that appear in both texts
print("words in common")

# Your code

# Creating count dictionary for common words and their absolute count
common_words = {}

# Sorting dictionary
common_words_sorted = []
if "alpha" in option:
    print("Option 1")  # Dummy Zeile

# Your code

elif "freq" in option:
    print("Option 2")  # Dummy Zeile

# Your code
else:
    common_words_sorted = common_words
    print("No valid sorting option was chosen. Data was not sorted.")

print("words in common:")
for item in common_words_sorted:
    print("common words")  # Dummy line
    # Your code
