import tkinter as tk
import random
import json
from tkinter import *
from PyDictionary import PyDictionary
from PIL import ImageTk, Image


# WORD_FILE contains a single object with it's properties being the word list; values don't matter
WORDS_FILE = 'words.txt'
DATABASE_FILE = 'words_dictionary.json'
MAX_GUESSES = 6

guess_number = 0 # Number of current guesses
meaning_generator = PyDictionary() # used to get meaning of words

# function to initialize the word database
def init_word_database(file_name):
    # Parse json file and create a dictionary from it
    word_dictionary = json.load(open(file_name))
    word_list = list(word_dictionary.keys()) # Create list with only the keys(words)
    # Filter out words that are not 5 letters long
    valid_word_list = list(filter(lambda word: True if len(word) == 5 else False, word_list))
    return list(map(lambda word: word.upper(), valid_word_list))

# Function to init the word list (from where the random word will be picked)
def words_list(file_name):
    with open(file_name, 'r') as f:
        word_list = f.read().splitlines()
    return list(map(lambda word: word.upper(), word_list))

# Function to check the correctness of the guessed word
def check_word(word_to_guess):
    global guess_number
    guessed_word = entry.get().upper()  # Get the guessed word from the entry field
    entry.delete(0, END)

    if (guess_number >= MAX_GUESSES):
        return
    if guessed_word not in database:
        print_message("This is not a valid word! Try again!")
        return

    for i, letter in enumerate(word_to_guess):
        if i < len(guessed_word) and guessed_word[i] == letter:
            labels[i + guess_number * 5].config(bg="green", text=guessed_word[i].upper())  # Correct letter at the correct position
            letters[ord(letter) - ord('A')].config(bg="green")
        elif guessed_word[i] in word_to_guess:
            labels[i + guess_number * 5].config(bg="yellow", text=guessed_word[i].upper())  # Correct letter, but at the wrong position
            letters[ord(guessed_word[i]) - ord('A')].config(bg="#E88900")
        else:
            labels[i + guess_number * 5].config(bg="gray", text=guessed_word[i].upper())  # Incorrect letter
            letters[ord(guessed_word[i]) - ord('A')].config(bg="#323232")

    guess_number += 1
    if (guessed_word == word_to_guess):
        guess_number = MAX_GUESSES + 1
        game_over(meaning_generator.meaning(word_to_guess), "win")
    if (guess_number == MAX_GUESSES):
        game_over(word_to_guess, "lost")
    
def game_over(word, outcome):
    if outcome == "lost":
        print_message(f"Game over! The word was {word}!")
    else:
        print_message(f"You guessed the word!\nGreat job! The word has the following meaning:\n{word}")

def print_message(message):
    messages.delete('1.0', END)
    messages.insert(INSERT, message)

word_list = words_list(WORDS_FILE) # List containing guessing words
database = init_word_database(DATABASE_FILE) # List containing valid words
word_to_guess = random.choice(word_list)
# Get a random word for which we have a meaning from the dictionary
while meaning_generator.meaning(word_to_guess, True) is None:
    word_to_guess = random.choice(word_list)
print(word_to_guess) # For testing purposes :)

# Create the main window
window = tk.Tk()
window.title("Wordle")
window.attributes('-fullscreen', True)
window.config(bg="#484848")


title_frame = tk.Frame(window, pady=20, bg="#1F1F1F")
title_frame.grid(column=0, row=0)

title = tk.Label(title_frame, width=62, bg="#1F1F1F", fg="white", anchor="center", font=("Neua Helvetica", 36), text="WORDĂL")
title.grid(row=0, column=0)

# Create a frame for logs
log = tk.Frame(window, width=20)
log.grid(column=0, row=2)

scroll_bar = tk.Scrollbar(log, orient="vertical")
scroll_bar.pack(side=RIGHT, fill='y')
messages = tk.Text(log, height=6, width=70, bg="#484848", font=("Neua Helvetica", 22), fg="white", yscrollcommand=scroll_bar.set, wrap=WORD)
print_message("Please enter a 5-letter word!")
scroll_bar.config(command=messages.yview)
messages.pack(side=LEFT)

content = tk.Frame(window, pady=50)
content.grid(column=0, row=1)
content.config(bg="#484848")

keyboard_frame = tk.Frame(window)
keyboard_frame.grid(column=0, row=1, sticky="w", padx=175)
keyboard_frame.lower()
letters = []
index = 0
for i in range(9):
    for j in range(3):
        if index < 26:
            letter = tk.Label(keyboard_frame, width=5, height=3, font=("Arial", 12, "bold"), bg="#979797", fg="white")
            letter.config(text=chr(ord('A') + index))
            index += 1
            letter.grid(row = i, column=j, padx=5, pady=5)
            letters.append(letter)

image_frame = tk.Frame(window)
image_frame.grid(column=0, row=1, sticky="e", padx=100)
img_right = ImageTk.PhotoImage(Image.open("cat_right.jpeg").resize((500, 500)))
right_panel = tk.Label(image_frame, image=img_right, bg="#484848")
right_panel.grid(column = 1, row = 0, sticky='e')
# Create a list to store the labels for each letter
labels = []

# Create labels for each letter in the word to be guessed
for j in range(1, MAX_GUESSES + 1):
    for i in range(5):  # Replace 5 with the length of the actual word to be guessed
        label = tk.Label(content, width=4, height=2, font=("Arial", 20), relief="solid", bg="white")
        label.grid(row=j, column=i, padx=5, pady=5)
        labels.append(label)


# Create an entry field for the user to input their guessed word
entry = tk.Entry(content, font=("Arial", 22))
entry.grid(row=MAX_GUESSES + 1, columnspan=5, padx=10, pady=20)

# Create a button to check the guessed word
button_frame=tk.Frame(content, bg="black")
button_frame.grid(row=MAX_GUESSES + 2, columnspan=5)

button = tk.Button(button_frame, text="Check", command=lambda: check_word(word_to_guess), height=3, width=10, font=("Neua Helvetica", 16, 'bold'))
button.grid(row=MAX_GUESSES + 2, columnspan=5, padx=10, pady=10, column=0)

quit_button = tk.Button(button_frame, text="EXIT", command=window.destroy, height=3, width=10, font=("Neua Helvetica", 16, 'bold'))
quit_button.grid(row = MAX_GUESSES + 2, columnspan=5, padx=10, pady=10, column=6)

window.mainloop()

