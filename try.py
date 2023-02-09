import random
import time


def hangman(word):
    word_list = list(word)
    word_len = len(word_list)
    display = ["_"] * word_len
    guessed = []
    tries = 6
    print("Welcome to Hangman! You have 6 tries to guess the word.")
    print(" ".join(display))

    while tries > 0:
        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        elif guess in word_list:
            indices = [i for i, x in enumerate(word_list) if x == guess]
            for index in indices:
                display[index] = guess
            word_list = [x for x in word_list if x != guess]
            print(" ".join(display))
        else:
            tries -= 1
            print("Incorrect. You have", tries, "tries left.")
            print(" ".join(display))
        if "_" not in display:
            print("You won! The word was", word)
            break
        guessed.append(guess)

    if tries == 0:
        print("You lost! The word was", word)


def merge_sort(word_list):
    if len(word_list) > 1:
        mid = len(word_list) // 2
        left = word_list[:mid]
        right = word_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                word_list[k] = left[i]
                i += 1
            else:
                word_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            word_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            word_list[k] = right[j]
            j += 1
            k += 1

    return word_list


def quick_sort(word_list, start, end):
    if start < end:
        pivot = partition(word_list, start, end)
        quick_sort(word_list, start, pivot - 1)
        quick_sort(word_list, pivot + 1, end)

    return word_list


def partition(word_list, start, end):
    pivot = word_list[end]
    i = start - 1
    for j in range(start, end):
        if word_list[j] <= pivot:
            i += 1
            word_list[i], word_list[j] = word_list[j], word_list[i]
    word_list[i + 1], word_list[end] = word_list[end], word_list[i + 1]
    return i + 1

def insertion_sort(word_list):
    for i in range(1, len(word_list)):
        key = word_list[i]
        j = i - 1
    while j >= 0 and key < word_list[j]:
        word_list[j + 1] = word_list[j]
        j -= 1
        word_list[j + 1] = key
        return word_list

def selection_sort(word_list):
    for i in range(len(word_list)):
        min_index = i
    for j in range(i + 1, len(word_list)):
        if word_list[j] < word_list[min_index]:
            min_index = j
            word_list[i], word_list[min_index] = word_list[min_index], word_list[i]
            return word_list

def bubble_sort(word_list):
    for i in range(len(word_list)):
        for j in range(0, len(word_list) - i - 1):
            if word_list[j] > word_list[j + 1]:
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]
                return word_list

def sort_word(word, sort_algorithm):
    word_list = list(word)
    if sort_algorithm == "merge_sort":
        return "".join(merge_sort(word_list))
    elif sort_algorithm == "quick_sort":
        return "".join(quick_sort(word_list, 0, len(word_list) - 1))
    elif sort_algorithm == "insertion_sort":
        return "".join(insertion_sort(word_list))
    elif sort_algorithm == "selection_sort":
        return "".join(selection_sort(word_list))
    elif sort_algorithm == "bubble_sort":
        return "".join(bubble_sort(word_list))
    else:
        print("Invalid sort algorithm")

def main():
    with open("words.txt", "r") as file:
        words = file.readlines()
        words = [word.strip() for word in words]
        random_word = random.choice(words)
        sorted_word = sort_word(random_word, "bubble_sort")
        start = time.time()
        hangman(sorted_word)
        end = time.time()
    print("Time taken:", end - start, "seconds")

if __name__ == '__main__':
    main()