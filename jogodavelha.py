import tkinter as tk
from tkinter import simpledialog, messagebox

class Game:
    def __init__(self):
        self.player1_name = ""
        self.player2_name = ""
        self.player1_symbol = 'X'
        self.player2_symbol = 'O'
        self.current_player = self.player1_symbol
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title("Jogo da Velha")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.get_player_names()

    def get_player_names(self):
        self.player1_name = simpledialog.askstring("Nome do Jogador 1", "Digite o nome do jogador 1 (X):")
        self.player2_name = simpledialog.askstring("Nome do Jogador 2", "Digite o nome do jogador 2 (O):")
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('normal', 20), width=5, height=2,
                                                command=lambda row=i, col=j: self.play(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def play(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                winner = self.player1_name if self.current_player == self.player1_symbol else self.player2_name
                messagebox.showinfo("Resultado", f"Parabéns {winner}! Você ganhou!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Resultado", "Empate!")
                self.reset_board()
            else:
                self.current_player = self.player1_symbol if self.current_player == self.player2_symbol else self.player2_symbol

    def check_winner(self, row, col):
        # Verificar linhas e colunas
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player:
            return True
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
            return True
        # Verificar diagonais
        if row == col:
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
                return True
        if row + col == 2:
            if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
                return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')
        self.current_player = self.player1_symbol

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Game()
    game.run()