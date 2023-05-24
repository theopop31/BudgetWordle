import tkinter as tk
from tkinter import *
MAX_GUESSES = 6
guess_number = 0
# Function to check the correctness of the guessed word
def check_word():
    global guess_number
    guessed_word = entry.get().lower()  # Get the guessed word from the entry field
    word_to_guess = "apple"  # Replace with the actual word to be guessed
    for i, letter in enumerate(word_to_guess):
        if i < len(guessed_word) and guessed_word[i] == letter:
            labels[i + guess_number * 5].config(bg="green", text=guessed_word[i].upper())  # Correct letter at the correct position
        elif guessed_word[i] in word_to_guess:
            labels[i + guess_number * 5].config(bg="yellow", text=guessed_word[i].upper())  # Correct letter, but at the wrong position
        else:
            labels[i + guess_number * 5].config(bg="gray", text=guessed_word[i].upper())  # Incorrect letter
    guess_number += 1

# Create the main window
window = tk.Tk()
window.title("Wordle")
window.attributes('-fullscreen', True)
window.config(bg="#484848")


title_frame = tk.Frame(window, bg="black", pady=20)
title_frame.grid(column=0, row=0)

title = tk.Label(title_frame, width=65, bg="black", fg="white", anchor="center", font=("Neua Helvetica", 36), text="WORDĂL", padx=5)
title.grid(row=0, column=0)

content = tk.Frame(window, pady=20)
content.grid(column=0, row=1)
content.config(bg="#484848")
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
button = tk.Button(content, text="Check", command=lambda: check_word(), height=3, width=10)
button.grid(row=MAX_GUESSES + 2, columnspan=5, padx=10, pady=10)

quit_button = tk.Button(content, text="EXIT", command=window.destroy, height=3, width=10)
quit_button.grid(row = MAX_GUESSES + 3, columnspan=5, padx=10, pady=10)

# Run the main event loop
window.mainloop()
