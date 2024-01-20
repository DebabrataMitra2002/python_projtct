import numpy as np
import random
from time import sleep

def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
        if win == True:
            return win
    return win

def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win == True:
            return win
    return win

def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board, player) or
            diag_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def print_board(board):
    for row in board:
        print(' '.join(['X' if cell == 1 else 'O' if cell == 2 else '-' for cell in row]))

def player_move(board):
    row = int(input("Enter the row (0, 1, 2): "))
    col = int(input("Enter the column (0, 1, 2): "))
    while board[row][col] != 0:
        print("Cell already filled. Pick another cell.")
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
    board[row][col] = 1
    return board

def computer_move(board):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = 2
    return board

def play_game():
    board = create_board()
    winner = 0
    counter = 1
    print("Initial board:")
    print_board(board)
    sleep(1)

    while winner == 0:
        if counter % 2 == 1:
            board = player_move(board)
        else:
            print("Computer's turn:")
            sleep(1)
            board = computer_move(board)
        print("Board after move", counter)
        print_board(board)
        sleep(1)
        winner = evaluate(board)
        if winner != 0:
            break
        counter += 1

    if winner == -1:
        print("It's a tie!")
    elif winner == 1:
        print("Player wins!")
    elif winner == 2:
        print("Computer wins!")

play_game()


