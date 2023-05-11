import colorama
colorama.init(autoreset=True)
from colorama import Fore, Back, Style

from functions import app_start, allowed_attempts, word_candidates, word_length, display, sort_words, word_entered, user_response, close

try:
    app_start()
    while True:
        for attempt in range(1, allowed_attempts + 1):
            temp_list = tuple(word_candidates)
            print(f"\n\n{Style.BRIGHT}{Fore.MAGENTA}Attempt {attempt} with {len(word_candidates)} possible words")
            print(f"\nHere are the best choices out of {len(word_candidates)} possible words calculated based on the frequency of letters in the Wordle word bank.")
            display(sort_words(word_candidates)[:6])
            guess = word_entered()
            feedback = user_response()
            if feedback == "GGGGG" and attempt == 1:
                print(f"\nAmazing effort! Guessing the Wordle in {attempt} attempt... What's your secret?")
                break
            elif feedback == "GGGGG":
                print(f"\nWell done! Solving today's Wordle took {attempt} attempts.")
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
            if attempt < allowed_attempts:
                counter = 0
                print("\nWord possibilities:")
                for word in word_candidates:
                    print(word, end = " | ")
                    counter += 1
                    if counter == 10:
                        print("")
                        counter = 0
        if feedback == "GGGGG":
            print(f"\n{close}")
        else:
            print(f"\nNo one said it would be easy. {close}")
        break
except KeyboardInterrupt:
    print(f"\n{close} See you next time.")