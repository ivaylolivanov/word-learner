#!/usr/bin/env python3

import os
import sys
import json


def ucfirst(string):
    result = ''.join([
        string[0].upper(),
        string[1:].lower()
    ])

    return result


def load_file(path):
    content = ''
    with open(path) as filestream:
        content = filestream.read()

    return content


translate_language = ucfirst(sys.argv[1])
dictionary_filepath = os.path.abspath(sys.argv[2])

dictionary = json.loads(load_file(dictionary_filepath))

correct   = []
incorrect = []

for word in dictionary:
    answer = input("How would you translate '{}' in '{}'?\n".format(
        word, translate_language
    ))

    translations = [
        translation.lower() for
        translation in dictionary[word]["Translations"][translate_language]
    ]

    if answer in translations:
        correct.append(''.join([word, ' - ', answer]))
    else:
        incorrect.append(''.join([word, ' - ', answer]))

print("Correct translations:\n{}\n\n".format(', '.join(correct)))
print("Incorrect translations:\n{}\n\n".format(', '.join(incorrect)))
