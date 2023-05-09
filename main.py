































# from collections import Counter
# from itertools import chain
# import operator
# from datetime import date
# import colorama
# colorama.init(autoreset=True)
# from colorama import Fore, Back, Style

# word_length = 5
# guesses = 6

# # Import all possible Wordle words from word-bank.txt
# word_candidates = []
# with open("word-bank.txt") as words:
#     for line in words:
#         word_candidates.append(line.strip())

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


# def app_start():
#     today = date.today()
#     formatted_date = today.strftime("%B %d, %Y")
#     print(f"\n{Style.BRIGHT}Welcome to Wordle Helper.\n")
#     print(f"Head to {Fore.MAGENTA}https://www.nytimes.com/games/wordle/index.html{Style.RESET_ALL} and let's get started with the daily Wordle for {formatted_date}!")
#     print(f"When you enter each result, remember the code: {Fore.GREEN}G for Green {Fore.YELLOW}Y for Yellow {Style.RESET_ALL}and X for Gray.")
#     print("\n----------------------------------------------------------------\n")

# def word_entered():
#     word = input("Word entered: ")
#     return word.lower()

# def user_response():
#     response = input("Wordle response (G|Y|X format): ")
#     return response.upper()

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