import random
from datetime import date
import colorama
colorama.init(autoreset=True)
from colorama import Fore, Back, Style
from collections import Counter
from itertools import chain
import operator

word_candidates = []
allowed_attempts = 6
word_length = 5
allowed_code = ("G", "Y", "X")
exit_prompt = "Type 'q' at any point if you want to quit the app."

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

def app_start():
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    print(f"\n{Style.BRIGHT}Welcome to Wordle Helper.\n")
    print(f"Head to {Fore.MAGENTA}https://www.nytimes.com/games/wordle/index.html{Style.RESET_ALL} and let's get started with the daily Wordle for {formatted_date}!")
    print(f"When you enter each result, remember the code: {Style.BRIGHT}{Fore.GREEN}G for Green {Fore.YELLOW}Y for Yellow {Fore.WHITE}X for Gray.")
    print(f"{exit_prompt}")
    print(f"\nHere are some random words from Wordle's word bank you might like to choose from: \n{random.choices(word_candidates, k=8)}")
    print("\n----------------------------------------------------------------")

def calculate_word_commonality(word):
    score = 0.0
    for letter in word:
        score += letter_frequency[letter]
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
    while True:
        word = input("\nWord entered: ")
        if word.lower() == "q":
            raise KeyboardInterrupt
        if not word.isalpha():
            print(f"Please enter letters only. {exit_prompt}")
            continue
        elif len(word) != word_length:
            print(f"Please enter a 5 letter word only. {exit_prompt}")
            continue
        else:
            return word.lower()
        
def contains_illegal_letter(word):
    for letter in word.upper():
        if letter not in allowed_code:
            return True

def user_response():
    while True:
        response = input(f"\nWordle response in {Style.BRIGHT}{Fore.GREEN}G{Fore.YELLOW}Y{Fore.WHITE}X {Style.RESET_ALL}formatting: ")
        if response.lower() == "q":
            raise KeyboardInterrupt
        if not response.isalpha():
            print(f"Please enter letters only. {exit_prompt}")
            continue
        elif len(response) != word_length:
            print(f"Please enter a 5 letter code. {exit_prompt}")
            continue
        elif contains_illegal_letter(response):
            print(f"There's a mistake with your input. Remember: {Style.BRIGHT}{Fore.GREEN}G for Green {Fore.YELLOW}Y for Yellow {Fore.WHITE}X for Gray.{Style.RESET_ALL} {exit_prompt}")
            continue
        else:
            return response.upper()