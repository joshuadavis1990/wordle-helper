from collections import Counter
from itertools import chain
import operator
from datetime import date
import colorama
colorama.init(autoreset=True)
from colorama import Fore, Back, Style

word_length = 5
guesses = 6

# Import all possible Wordle words from word-bank.txt
word_candidates = []
with open("word-bank.txt") as words:
    for line in words:
        word_candidates.append(line.strip())

# Algorithm to find most common letters in word-bank.txt
letter_counter = Counter(chain.from_iterable(word_candidates))

# Algorithm to split most common letters into percentages of the overall total
letter_frequency = {
    character: value / letter_counter.total()
    for character, value in letter_counter.items()
}

# Word scoring function for commonality of letters in word
def word_commonality(word):
    score = 0.0
    for character in word:
        score += letter_frequency[character]
    return score / (word_length - len(set(word)) + 1)

# Sorts and displays words to user
def sort_by_word_commonality(words):
    sort_by = operator.itemgetter(1)
    return sorted(
        [(word, word_commonality(word)) for word in words],
        key=sort_by,
        reverse=True,
    )

def display_word_table(word_commonalities):
    for (word, freq) in word_commonalities:
        print(f"{word:<10} | {freq:<5.2}")

# print(display_word_table(sort_by_word_commonality(word_candidates)))

def app_start():
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    print(f"\n{Style.BRIGHT}Welcome to Wordle Helper.\n")
    print(f"Head to {Fore.MAGENTA}https://www.nytimes.com/games/wordle/index.html{Style.RESET_ALL} and let's get started with the daily Wordle for {formatted_date}!")
    print(f"When you enter each result, remember the code: {Fore.GREEN}G for Green {Fore.YELLOW}Y for Yellow {Style.RESET_ALL}and X for Gray.")
    print("\n----------------------------------------------------------------\n")

def word_entered():
    word = input("Word entered: ")
    return word.lower()

def user_response():
    response = input("Wordle response: ")
    return response.upper()

def find_g_index():
    list = []
    for index, letter in enumerate(user_response):
        if letter == "G":
            list.append(index)
    return list

app_start()
word_entered = word_entered()
user_response = user_response()
g_index = find_g_index()
print(g_index)

def find_g():
    for words in word_candidates:
        








# PSEUDOCODE

# The purpose of this application is to assist the user in solving the daily Wordle challenge at https://www.nytimes.com/games/wordle/index.html. In order to meet the assessment brief, it will need to include: user input, printed output, variables and variable scope, loops and conditional control structures, six or more simple functions, error handling, four or more Python packages, functions from one or more Python packages, and two tests.

# First iteration of app - focus on correct letters only:
# - Import a dictionary or list of words - narrow words to 5 letter words only
# - User enters their first guess
# - User enters their results in a defined format, e.g. Y = correct, N = incorrect e.g. YYNNY?
# - Iterate through the word list/imported dictionary to find words that match the pattern the user has input
# - Repeat the above process six times or until the correct word is found
# - Remind user to type quit to exit the app at any point

# TEST FUNCTIONS

def choose_letter(letter):
    for word in word_candidates:
        if letter.lower() in word:
            print(word)
# choose_letter(input("What letter must the word contain? "))

def choose_letters(a, b, c):
    for word in word_candidates:
        if a.lower() in word and b.lower() in word and c.lower() in word:
            print(word)
# choose_letters("A", "V", "E")

def first_letter(a):
    for word in word_candidates:
        if word[0] == a.lower():
            print(word)
# first_letter("g")

def letter_positions(let1, let1_position, let2, let2_position):
    for word in word_candidates:
        if word[let1_position - 1] == let1.lower() and word[let2_position - 1] == let2.lower():
            print(word)

# let1 = input("Letter 1: ")
# let1_position = int(input("Position: "))
# let2 = input("Letter 2: ")
# let2_position = int(input("Position: "))
# letter_positions(let1, let1_position, let2, let2_position)