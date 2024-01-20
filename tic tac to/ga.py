def print_board(board):
    # Prints the current state of the board
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_win(board):
    # Checks if there is a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]
    else:
        return None

def check_tie(board):
    # Checks if the game is tied
    for row in board:
        if "-" in row:
            return False
    return True

def make_move(board, player, row, col):
    # Makes a move on the board
    if board[row][col] == "-":
        board[row][col] = player
        return True
    else:
        print("Invalid move. Please try again.")
        return False

def tic_tac_toe():
    # The main function to play Tic Tac Toe
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}, it's your turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if make_move(board, current_player, row, col):
            print_board(board)
            winner = check_win(board)
            if winner:
                print(f"Congratulations, Player {winner} wins!")
                break
            elif check_tie(board):
                print("It's a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"

tic_tac_toe()