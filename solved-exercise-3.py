#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import sys
import re
import os
from collections import Counter, OrderedDict

file_1 = 'Texte/text1_tokenized.txt'
file_2 = 'Texte/text2_tokenized.txt'

# read file or string in argument
def read_file(document):
    if not os.path.exists(document):
        return document
    with open(document, 'r') as text_file:
        text = text_file.read()
    return text

# read file -> separate it by words and count how many times each word repeat
def to_dict_with_count(text_file):
    text = read_file(text_file)
    text_list = re.findall(r'\S+', text)
    return Counter(text_list)

# order dict by word
def order_by_name(some_dict):
    return OrderedDict(sorted(some_dict.items(), key=lambda t: t[0].lower()))

# order dict by count of words in text from max to min
def order_by_value(some_dict):
    return OrderedDict(sorted(some_dict.items(), key=lambda t: t[1], reverse=True))

# compare two or more texts and print words that occur in each text
def compare_dicts(list_name, list_dict):
    print("words in common")
    length = len(list_dict)
    new_dict = {}
    for key in list_dict[0]:
        new_dict[key] = ['{}: {}'.format(list_name[0], list_dict[0][key])]
        for i in range(1, len(list_dict)):
            if key in list_dict[i]:
                new_dict[key].append('{}: {}'.format(list_name[i], list_dict[i][key]))
    for key in list_dict[0]:
        if len(new_dict[key]) == length:
            print(key, '--', *new_dict[key])


def main(list_of_files, option=False):
    all_dicts = []
    if option == 'alpha':
        print("Option 1")
        all_dicts.append(order_by_name(to_dict_with_count(list_of_files[0])))
        for text_file in list_of_files[1:]:
            all_dicts.append(to_dict_with_count(text_file))
    elif option == 'freq':
        print("Option 2")
        all_dicts.append(order_by_value(to_dict_with_count(list_of_files[0])))
        for text_file in list_of_files[1:]:
            all_dicts.append(to_dict_with_count(text_file))
    else:
        print("No valid sorting option was chosen. Data was not sorted.")
        all_dicts = [to_dict_with_count(text_file) for text_file in list_of_files]
    compare_dicts(list_of_files, all_dicts)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg_list = []
        option = False
        for argv in sys.argv[1:]:
            if argv in ('--alpha', '--freq'):
                option = argv[2:]
            else:
                arg_list.append(argv)
        main(arg_list, option)
    else:
        first_dict = to_dict_with_count(file_1)
        second_dict = to_dict_with_count(file_2)
        compare_dicts([file_1, file_2], [first_dict, second_dict])