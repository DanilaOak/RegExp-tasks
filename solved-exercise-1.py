#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import re
import sys
import os

# Dictionary of irregular verbs
irregulars = {"mimick": "mimic", "reli": "rely", "withheld": "withhold", "locat": "locate"}

# default file with arguments
document = 'Texte/verbs.txt'


# Read in arguments
def make_list(name):
    verbs_list = []
    if not os.path.exists(name):
        return [name]
    with open(name, 'r') as text_file:
        for line in text_file:
            verbs_list.append(line.rstrip())
    return verbs_list


# Separate the trunk from the verb for each word
def stemmer(verbs_list):
    r = re.compile(r'(\w+)(s|ed|ing)$')
    for verb in verbs_list:
        search = r.match(verb)
        if search:
            begin = search.group(1)
            end = search.group(2)
            if begin in irregulars:
                reg = re.compile(r'(?<={})\w*[^({})]'.format(irregulars[begin], end))
                center = reg.findall(verb)
                print(verb, '->', irregulars[begin], *center, end)
            else:
                print(verb, '->', begin, end)
        else:
            if verb in irregulars:
                print(verb, '->', irregulars[verb])
            else:
                print(verb, '->', verb)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for line in sys.argv[1:]:
            verb_list = make_list(line)
            stemmer(verb_list)
    else:
        verb_list = make_list(document)
        stemmer(verb_list)
