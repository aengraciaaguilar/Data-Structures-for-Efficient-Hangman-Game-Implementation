# Laboratory Activity # 8
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2

import random

def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    return words

