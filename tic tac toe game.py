import tkinter as tk
from tkinter import messagebox
from collections import deque
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [' '] * 9
        self.buttons = []
        self.vs_computer = True  # Default is player vs computer
        self.create_board()
        self.root.mainloop()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 20), width=6, height=3,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j, sticky='nsew')
                row.append(button)
            self.buttons.append(row)

        # Add a button for switching between player vs player and player vs computer
        self.mode_button = tk.Button(self.root, text='Switch to Player vs Player', font=('Arial', 12),
                                     command=self.switch_mode)
        self.mode_button.grid(row=3, columnspan=3, sticky='nsew')

    def on_click(self, i, j):
        if self.board[i * 3 + j] == ' ':
            self.board[i * 3 + j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.reset_board()
            elif ' ' not in self.board:
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            elif self.vs_computer and self.current_player == 'X':
                self.current_player = 'O'
                self.bfs_move()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def switch_mode(self):
        self.vs_computer = not self.vs_computer
        if self.vs_computer:
            self.mode_button.config(text='Switch to Player vs Player')
        else:
            self.mode_button.config(text='Switch to Player vs Computer')

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return True
        return False

    def bfs_move(self):
        queue = deque([(self.board[:], 'O')])
        while queue:
            board, player = queue.popleft()
            empty_indices = [i for i in range(9) if board[i] == ' ']
            random_index = random.choice(empty_indices)
            board[random_index] = player
            self.board[random_index] = player
            self.buttons[random_index // 3][random_index % 3].config(text=player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"{player} wins!")
                self.reset_board()
                return
            else:
                self.current_player = 'X'

    def reset_board(self):
        self.current_player = 'X'
        self.board = [' '] * 9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')

if __name__ == "__main__":
    game = TicTacToe()
