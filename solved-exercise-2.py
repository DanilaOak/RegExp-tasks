#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import re
import sys
import os

# text that must be annotated
annotates = {
    '_DOT': ['the', 'a', 'an', 'that'],
    '_PRON': ['I', 'you', 'he'],
    '_NUM': ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
}

# default file which will be annotated
doc = 'Texte/text1_tokenized.txt'


# Read in arguments
def read_file(document):
    if not os.path.exists(document):
        return document
    with open(document, 'r') as text_file:
        text = text_file.read()
    return text


# Create file with annotated text
def write_file(text):
    for annotate in annotates:
        for word in annotates[annotate]:
            if annotate == '_NUM':
                text = text.replace(' {} '.format(word), ' {}{} '.format(word, annotate))
                text = text.replace(' {}s '.format(word), ' {}s{} '.format(word, annotate))
            else:
                text = text.replace(' {} '.format(word), ' {}{} '.format(word, annotate))
    num_text = re.findall('\s\d+.?\d+?\s', text)
    for value in num_text:
        text = text.replace(value, ' {}{} '.format(value.rstrip(), '_NUM'))
    with open('annotated_t.txt', 'w+') as text_file:
        text_file.write(text)
    print('annotated text created')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for line in sys.argv[1:]:
            text_from_file = read_file(line)
            write_file(text_from_file)
    else:
        text_from_file = read_file(doc)
        write_file(text_from_file)
