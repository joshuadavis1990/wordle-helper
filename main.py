# PYTHON PACKAGES

import random
from datetime import date
import colorama
colorama.init(autoreset=True)
from colorama import Fore, Back, Style
from collections import Counter
from itertools import chain
import operator

# GLOBAL VARIABLES

guess = ""
feedback = ""
word_candidates = []
allowed_attempts = 6
word_length = 5

try:
    with open("word-bank.txt") as words:
        for line in words:
            word_candidates.append(line.strip())
except FileNotFoundError:
    print("File not found.")

letter_counter = Counter(chain.from_iterable(word_candidates))

letter_frequency = {
    character: value / letter_counter.total()
    for character, value in letter_counter.items()
}

# APP FUNCTIONS

def app_start():
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    print(f"\n{Style.BRIGHT}Welcome to Wordle Helper.\n")
    print(f"Head to {Fore.MAGENTA}https://www.nytimes.com/games/wordle/index.html{Style.RESET_ALL} and let's get started with the daily Wordle for {formatted_date}!")
    print(f"When you enter each result, remember the code: {Style.BRIGHT}{Fore.GREEN}G for Green {Fore.YELLOW}Y for Yellow {Fore.WHITE}X for Gray.")
    print(f"\nHere are some random words from Wordle's word bank you might like to choose from: \n{random.choices(word_candidates, k=8)}")
    print("\n----------------------------------------------------------------")

def calculate_word_commonality(word):
    score = 0.0
    for char in word:
        score += letter_frequency[char]
    return score / (word_length - len(set(word)) + 1)

def sort_words(words):
    sort = operator.itemgetter(1)
    return sorted(
        [(word, calculate_word_commonality(word)) for word in words],
        key = sort,
        reverse = True,
    )

def display(word_commonalities):
    for word, distribution in word_commonalities:
        print(f"{word:<10} | {distribution:<5.2}")

def word_entered():
    word = input("Word entered: ")
    if type(word) is int:
        raise TypeError("Please enter a 5-letter word only.")
    return word.lower()

def user_response():
    response = input(f"Wordle response in {Style.BRIGHT}{Fore.GREEN}G{Fore.YELLOW}Y{Fore.WHITE}X {Style.RESET_ALL}formatting: ")
    return response.upper()

# MAIN CODE

app_start()
for attempt in range(1, allowed_attempts + 1):
    temp_list = tuple(word_candidates)
    print(f"\n\n{Style.BRIGHT}{Fore.MAGENTA}Attempt {attempt} with {len(word_candidates)} possible words")
    display(sort_words(word_candidates)[:15])
    guess = word_entered()
    feedback = user_response()
    if feedback == "GGGGG" and attempt == 1:
        print(f"\nAmazing effort! You only took {attempt} attempt! What's your secret?")
        break
    elif feedback == "GGGGG":
        print(f"\nWell done! You took {attempt} attempts!")
        break
    for word in temp_list:
        for i in range(word_length):
            if feedback[i] == "X" and guess[i] in word:
                word_candidates.remove(word)
                break
            elif feedback[i] == "G" and guess[i] != word[i]:
                word_candidates.remove(word)
                break
            elif feedback[i] == "Y" and guess[i] not in word:
                word_candidates.remove(word)
                break
            elif feedback[i] == "Y" and guess[i] == word[i]:
                word_candidates.remove(word)
                break
    counter = 0
    print("\nWord possibilities:")
    for word in word_candidates:
        print(word, end = " | ")
        counter += 1
        if counter == 10:
            print("")
            counter = 0