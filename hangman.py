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

def merge_sort(words):
    if len(words) <= 1:
        return words
    mid = len(words) // 2
    left = merge_sort(words[:mid])
    right = merge_sort(words[mid:])
    return merge(left, right)

def bubble_sort(words):
    for i in range(len(words)):
        for j in range(len(words) - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]
    return words
