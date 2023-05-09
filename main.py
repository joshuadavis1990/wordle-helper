from datetime import date
import colorama
colorama.init(autoreset=True)
from colorama import Fore, Back, Style

guess = ""
feedback = ""
word_candidates = []

def app_start():
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    print(f"{Style.BRIGHT}Welcome to Wordle Helper.\n")
    print(f"Head to {Fore.MAGENTA}https://www.nytimes.com/games/wordle/index.html{Style.RESET_ALL} and let's get started with the daily Wordle for {formatted_date}!")
    print(f"When you enter each result, remember the code: {Style.BRIGHT}{Fore.GREEN}G for Green {Fore.YELLOW}Y for Yellow {Fore.WHITE}X for Gray.")
    print("\n----------------------------------------------------------------\n")

def word_entered():
    word = input("Word entered: ")
    if type(word) is str:
        raise TypeError("Please enter a 5-letter word only.")
    return word.lower()

def user_response():
    response = input(f"Wordle response in {Style.BRIGHT}{Fore.GREEN}G{Fore.YELLOW}Y{Fore.WHITE}X {Style.RESET_ALL}formatting: ")
    return response.upper()

try:
    with open("word-bank.txt") as words:
        for line in words:
            word_candidates.append(line.strip())
except FileNotFoundError:
    print("File not found.")

app_start()
for guesses in range(6):
    guess = word_entered()
    feedback = user_response()
    if feedback == "GGGGG":
        print("Well done!")
        break
    temp_list = tuple(word_candidates)
    for word in temp_list:
        for i in range(5):
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
    print("The solution is one of the following words:")
    for word in word_candidates:
        print(word,end=" ")
        counter += 1
        if counter == 10:
            print("")
            counter = 0










# from collections import Counter
# from itertools import chain
# import operator

# # Algorithm to find most common letters in word-bank.txt
# letter_counter = Counter(chain.from_iterable(word_candidates))

# # Algorithm to split most common letters into percentages of the overall total
# letter_frequency = {
#     character: value / letter_counter.total()
#     for character, value in letter_counter.items()
# }

# # Word scoring function for commonality of letters in word
# def word_commonality(word):
#     score = 0.0
#     for character in word:
#         score += letter_frequency[character]
#     return score / (word_length - len(set(word)) + 1)

# # Sorts and displays words to user
# def sort_by_word_commonality(words):
#     sort_by = operator.itemgetter(1)
#     return sorted(
#         [(word, word_commonality(word)) for word in words],
#         key=sort_by,
#         reverse=True,
#     )

# def display_word_table(word_commonalities):
#     for (word, freq) in word_commonalities:
#         print(f"{word:<10} | {freq:<5.2}")




# def match_word_candidates_copy(word, word_candidates_copy):
#     for letter, v_letter in zip(word, word_candidates_copy):
#         if letter not in v_letter:
#             return False
#     return True

# def match(word_candidates_copy, word_candidates):
#     return [word for word in word_candidates if match_word_candidates_copy(word, word_candidates_copy)]

# def solve():
#     word_candidates = []
#     with open("word-bank.txt") as words:
#         for line in words:
#             word_candidates.append(line.strip())
#     word_candidates_copy = [word_candidates for _ in range(word_length)]
#     app_start()
#     for attempt in range(1, guesses + 1):
#         print(f"Attempt {attempt} with {len(word_candidates)} possible words")
#         display_word_table(sort_by_word_commonality(word_candidates)[:15])
#         word = word_entered()
#         response = user_response()
#         for index, letter in enumerate(response):
#             if letter == "G":
#                 word_candidates_copy[index] = {word[index]}
#             # elif letter == "Y":
#             #     try:
#             #         word_candidates_copy[index].remove(word[index])
#             #     except KeyError:
#             #         pass
#             # elif letter == "X":
#             #     for value in word_candidates_copy:
#             #         try:
#             #             value.remove(word[index])
#             #         except KeyError:
#             #             pass
#     word_candidates = match(word_candidates_copy, word_candidates)

# solve()