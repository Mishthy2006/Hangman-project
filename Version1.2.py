import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("400x300")

        self.secret_word = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6

        self.word_label = tk.Label(master, text=self.display_word(), font=('Arial', 18), fg='blue')
        self.word_label.pack(pady=10)

        self.guess_label = tk.Label(master, text="Guessed Letters: ", font=('Arial', 14), fg='green')
        self.guess_label.pack()

        self.attempts_label = tk.Label(master, text=f"Attempts left: {self.attempts}", font=('Arial', 14), fg='red')
        self.attempts_label.pack()

        self.guess_entry = tk.Entry(master, font=('Arial', 14))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess, font=('Arial', 14), bg='orange', fg='white')
        self.guess_button.pack()

    def choose_word(self):
        words = ["python", "hangman", "programming", "challenge", "developer", "coding"]
        return random.choice(words)

    def display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    def draw_hangman(self):
        # Implement your hangman graphics here if needed
        pass

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in self.guessed_letters:
                self.show_message("You've already guessed that letter. Try again.")
            elif guess in self.secret_word:
                self.show_message("Good guess!")
                self.guessed_letters.append(guess)
            else:
                self.show_message("Incorrect guess!")
                self.attempts -= 1
                self.guessed_letters.append(guess)
        else:
            self.show_message("Invalid input. Please enter a single letter.")

        self.update_display()

        if "_" not in self.display_word():
            self.end_game(True)
        elif self.attempts == 0:
            self.end_game(False)

    def update_display(self):
        self.word_label.config(text=self.display_word())
        self.guess_label.config(text=f"Guessed Letters: {', '.join(self.guessed_letters)}")
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

    def show_message(self, message):
        tk.messagebox.showinfo("Hangman Game", message)

    def end_game(self, win):
        if win:
            message = f"Congratulations! You've guessed the word: {self.secret_word}"
        else:
            message = f"Sorry, you ran out of attempts. The word was: {self.secret_word}"
        
        play_again = tk.messagebox.askyesno("Hangman Game", message + "\nDo you want to play again?")
        if play_again:
            self.reset_game()
        else:
            self.master.destroy()

    def reset_game(self):
        self.secret_word = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()
