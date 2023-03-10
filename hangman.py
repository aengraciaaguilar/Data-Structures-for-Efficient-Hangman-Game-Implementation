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

def insertion_sort(words):
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        while j >= 0 and key < words[j]:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key
    return words

def selection_sort(words):
    for i in range(len(words)):
        min_index = i
        for j in range(i + 1, len(words)):
            if words[j] < words[min_index]:
                min_index = j
        words[i], words[min_index] = words[min_index], words[i]
    return words

def partition(words, low, high):
    pivot = words[high]
    i = low - 1
    for j in range(low, high):
        if words[j] <= pivot:
            i = i + 1
            words[i], words[j] = words[j], words[i]
    words[i + 1], words[high] = words[high], words[i + 1]
    return i + 1

def quick_sort(words, low, high):
    if low < high:
        pivot = partition(words, low, high)
        quick_sort(words, low, pivot - 1)
        quick_sort(words, pivot + 1, high)
    return words

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def play_hangman():
    word = get_word()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    tries = 6
    print("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
    print("                        Hi Player! Ready to Play?                           ")
    print("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
    print("\n")
    print("             CLUE: the word contains", len(word_letters), "letters.")
    while len(word_letters) > 0 and tries > 0:
        print("           CHANCES: you still have", tries, "tries left.")
        if used_letters:
            print("\n"
                  "used letters:", " ".join(sorted(used_letters)))
        print("\n")
        print("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
        print("   AVAILABLE LETTERS:", " ".join(sorted(alphabet - used_letters)))
        print("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
        print(display_hangman(tries))
        guess = input("please enter a letter: ").lower()

        if guess in word_letters:
            word_letters.remove(guess)
            print("\n"
                  "nice! good guess:", end=" ")
            for letter in word:
                if letter in used_letters:
                    print(letter, end=" ")
                elif letter == guess:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("\n")
        elif guess in used_letters:
            print("you already used that letter, please try again.\n")
        else:
            print("\n"
                  "you entered a wrong letter, please try again.\n")
            tries -= 1
            used_letters.add(guess)
    if tries == 0:
        print("\n"
              "                                                       SORRY YOU LOST! the word was", word)
    else:
        print("CONGRATULATIONS YOU WON! you guessed this", word)


play_hangman()
