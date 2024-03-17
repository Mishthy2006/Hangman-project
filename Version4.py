import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("400x600")
        self.master.configure(bg="lightblue")

        self.heading_label = tk.Label(master, text="Hangman Game", font=("Arial", 20, "bold"), bg="lightblue")
        self.heading_label.pack()

        self.words = ['python', 'hangman', 'programming', 'code', 'computer', 'game', 'algorithm', 'project', 'data', 'binary', 'array', 'backend', 'byte', 'conditionals', 'iteration']
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts_left = 6
        self.score = 0  # Initialize score
        
        self.canvas = tk.Canvas(master, width=400, height=400, bg="lightblue")
        self.canvas.pack()

        self.draw_hangman()

        self.word_label = tk.Label(master, text=self.display_word(), font=("Arial", 24), bg="lightblue")
        self.word_label.pack()

        self.attempts_label = tk.Label(master, text=f"Attempts left: {self.attempts_left}", font=("Arial", 14), bg="lightblue")
        self.attempts_label.pack()

        self.guessed_label = tk.Label(master, text="Guessed Letters:", font=("Arial", 14), bg="lightblue")
        self.guessed_label.pack()

        self.letter_entry = tk.Entry(master, font=("Arial", 18))
        self.letter_entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, bg="orange", fg="white", font=("Arial", 14))
        self.guess_button.pack()

        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again, bg="green", fg="white", font=("Arial", 14))
        self.play_again_button.pack()

    def draw_hangman(self):
        self.canvas.create_line(50, 350, 150, 350, width=2, fill="blue")
        self.canvas.create_line(100, 350, 100, 100, width=2, fill="blue")
        self.canvas.create_line(100, 100, 200, 100, width=2, fill="blue")
        self.canvas.create_line(200, 100, 200, 150, width=2, fill="blue")

    def display_word(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += '_'
        return display

    def check_guess(self):
        guess = self.letter_entry.get()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Error", "Please enter a single letter.")
            return

        guess = guess.lower()
        if guess in self.guessed_letters:
            messagebox.showinfo("Info", "You've already guessed that letter.")
            return

        self.guessed_letters.append(guess)
        self.word_label.config(text=self.display_word())
        self.letter_entry.delete(0, tk.END)  # Clear the entry box after guessing

        if guess not in self.word:
            self.attempts_left -= 1
            self.draw_hangman_part()

        if '_' not in self.display_word():
            self.score += 10 * self.attempts_left  # Award points based on remaining attempts
            messagebox.showinfo("Congratulations", f"You've guessed the word: {self.word}. Your score: {self.score}.")
            self.play_again()

    def draw_hangman_part(self):
        parts = 6 - self.attempts_left
        if parts == 1:
            self.canvas.create_oval(180, 150, 220, 190, width=2, outline='blue')
        elif parts == 2:
            self.canvas.create_line(200, 190, 200, 290, width=2, fill='red')
        elif parts == 3:
            self.canvas.create_line(200, 200, 150, 250, width=2, fill='red')
        elif parts == 4:
            self.canvas.create_line(200, 200, 250, 250, width=2, fill='red')
        elif parts == 5:
            self.canvas.create_line(200, 290, 150, 340, width=2, fill='red')
        elif parts == 6:
            self.canvas.create_line(200, 290, 250, 340, width=2, fill='red')
            self.score -= 20  # Deduct points for game over
            messagebox.showinfo("Game Over", f"Sorry, you're out of attempts! The word was: {self.word}. Your score: {self.score}.")
            self.play_again()

        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.guessed_label.config(text=f"Guessed Letters: {' '.join(self.guessed_letters)}")

    def play_again(self):
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts_left = 6
        self.word_label.config(text=self.display_word())
        self.canvas.delete("all")
        self.draw_hangman()
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.guessed_label.config(text="Guessed Letters:")

def main():
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
