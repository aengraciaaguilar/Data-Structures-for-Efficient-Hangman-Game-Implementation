# Laboratory Activity # 8
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2

import random

def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    return words

def get_word():
    words = get_words_from_file("words.txt")
    return random.choice(words)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
