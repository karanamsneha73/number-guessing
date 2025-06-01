import tkinter as tk
from tkinter import *
import random

# Initialize the main window
win = tk.Tk()
win.geometry("750x750")
win.title("Sneha's Number Guessing Game")

# Variables
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()
num = random.randint(1, 50)
hint.set("Guess a number between 1 to 50")
score.set(5)
final_score.set(score.get())

# Function to generate clues
def generate_clue(number):
    clues = []
    if number % 2 == 0:
        clues.append("The number is even.")
    else:
        clues.append("The number is odd.")
    
    if number % 5 == 0:
        clues.append("It is a multiple of 5.")
    
    if number % 10 == 0:
        clues.append("It is a multiple of 10.")
    else:
        clues.append(f"The closest multiple of 10 is {10 * round(number / 10)}.")
    
    if number < 25:
        clues.append("The number is less than 25.")
    else:
        clues.append("The number is 25 or more.")
    
    return " ".join(clues)

# Function to handle guesses
def fun():
    x = guess.get()
    final_score.set(score.get())

    if score.get() > 0:
        if x < 1 or x > 50:
            hint.set("Invalid input! Please guess a number between 1 and 50. You lost 1 chance.")
            score.set(score.get() - 1)
        elif num == x:
            hint.set(f"Congratulations! You guessed it right in {5 - score.get()} tries!")
        elif num > x:
            clue = generate_clue(num)
            hint.set(f"Too low! {clue}")
            score.set(score.get() - 1)
        elif num < x:
            clue = generate_clue(num)
            hint.set(f"Too high! {clue}")
            score.set(score.get() - 1)
    else:
        hint.set(f"Game Over! The correct number was {num}.")

# Function to reset the game
def reset_game():
    global num
    num = random.randint(1, 50)
    score.set(5)
    hint.set("Guess a number between 1 to 50")
    guess.set(0)

# UI Elements
Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)
Entry(win, text=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

Label(win, text='I challenge you to guess the number', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
Label(win, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)
Button(win, width=8, text='RESET', font=('Courier', 25), command=reset_game, relief=GROOVE, bg='light green').place(relx=0.7, rely=0.5, anchor=CENTER)

# Run the main loop
win.mainloop()
