import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x300")
        self.window.configure(bg="#f0f0f0")  # light gray background

        self.player_turn = "X"
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), 
                                   height=3, width=6, font=("Helvetica", 24), bg="#ccc", 
                                   activebackground="#aaa", relief="ridge")
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset, 
                                      font=("Helvetica", 14), bg="#4CAF50", fg="#fff", 
                                      activebackground="#3e8e41", relief="ridge")
        self.reset_button.grid(row=3, column=1, padx=5, pady=5)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.reset()
            else:
                self.player_turn = "O" if self.player_turn == "X" else "X"


    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.reset()
            else:
                self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def reset(self):
        self.player_turn = "X"
        for row in self.buttons:
            for button in row:
                button['text'] = ""

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()