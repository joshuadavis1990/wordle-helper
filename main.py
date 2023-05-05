# The purpose of this application is to assist the user in solving the daily Wordle challenge at https://www.nytimes.com/games/wordle/index.html. In order to meet the assessment brief, it will need to include: user input, printed output, variables and variable scope, loops and conditional control structures, six or more simple functions, error handling, four or more Python packages, functions from one or more Python packages, and two tests.

# First iteration of app - focus on correct letters only:
# - Import a dictionary or list of words - narrow words to 5 letter words only
# - User enters their first guess
# - User enters their results in a defined format, e.g. Y = correct, N = incorrect e.g. YYNNY?
# - Iterate through the word list/imported dictionary to find words that match the pattern the user has input
# - Repeat the above process six times or until the correct word is found
# - Remind user to type quit to exit the app at any point

word_candidates = []
with open("word-bank.txt") as words:
    for line in words:
        word_candidates.append(line.strip())
# print(word_candidates[0:10])

# choose_a_word = "court"
# for word in word_candidates:
#     if word == choose_a_word:
#         print(word)

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
            
let1 = input("Letter 1: ")
let1_position = int(input("Position: "))
let2 = input("Letter 2: ")
let2_position = int(input("Position: "))
letter_positions(let1, let1_position, let2, let2_position)