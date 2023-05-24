import json
from PyDictionary import PyDictionary
import random

# WORD_FILE contains a single object with it's properties being the word list; values don't matter
WORDS_FILE = 'words.txt'
DATABASE_FILE = 'words_dictionary.json'
MAX_GUESSES = 6

meaning_generator = PyDictionary() # used to get meaning of words

# function to initialize the word database
def init_word_database(file_name):
    # parse json file and create a dictionary from it
    word_dictionary = json.load(open(file_name))
    word_list = list(word_dictionary.keys()) # create list with only the keys(words)
    # filter out words that are not 5 letters long
    valid_word_list = list(filter(lambda word: True if len(word) == 5 else False, word_list))
    return list(map(lambda word: word.upper(), valid_word_list))

# function to init the word list (from where the random word will be picked)
def words_list(file_name):
    with open(file_name, 'r') as f:
        word_list = f.read().splitlines()
    return list(map(lambda word: word.upper(), word_list))


def user_input(database):
    while True:
        guess = input("Enter a 5 letter word: ").upper()
        if guess not in database:
            print("Not a valid word! Try again")
            continue
        else:
            return guess

def game_over(word):
    print(f"Game over! The word was {word}!")

def main():
    #current_guesses = 1
    word_list = words_list(WORDS_FILE)
    database = init_word_database(DATABASE_FILE)
    word_to_guess = random.choice(word_list)
    while meaning_generator.meaning(word_to_guess, True) is None:
        word_to_guess = random.choice(word_list)
    print(word_to_guess)
    for current_guesses in range(MAX_GUESSES):
        guess = user_input(database)
        if guess == word_to_guess:
            print("Correct")
            print(meaning_generator.meaning(guess.lower()))
            break

        correct = {letter for letter , correct in zip(guess, word_to_guess) if letter == correct}
        misplaced = set(guess) & set(word_to_guess) - correct
        wrong = set(guess) - set(word_to_guess)

    if current_guesses > MAX_GUESSES:
        game_over(word_to_guess)

if __name__ == "__main__":
    main()



