import random

board = [" ", " ", " ", " "," ", " ", " ", " ", " ", " "]

def create_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    
def check_win(player):
    if (board[0] == player and board[1] == player and board[2] == player) or (board[3] == player and board[4] == player and board[5] == player) or (board[6] == player and board[7] == player and board[8] == player) or (board[0] == player and board[3] == player and board[6] == player) or (board[1] == player and board[4] == player and board[7] == player) or (board[2] == player and board[5] == player and board[8] == player):
        return True
    else:
        return False

def get_ai_move(player):
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_win(player):
                return i
            else:
                board[i] = " "
    
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if check_win(opponent):
                board[i] = player
                return i
            else:
                board[i] = " "
    
    while True:
        move = random.randint(0,8)
        if board[move] == " ":
            board[move] = player
            return move

while True:
    create_board()
    player_move = int(input("Enter you position:(0-8)"))
    while board[player_move] != " ":
        print("Move already taken!")
        player_move = int(input("Enter you position:(0-8)"))
    board[player_move] = "X"
    if check_win("X"):
        create_board()
        print("You won!!!")
        break
    ai_move = get_ai_move("O")
    board[ai_move] = "O"
    if check_win("O"):
        create_board()
        print("AI won!!!")
        break
    if " " not in board:
        create_board()
        print("Draw!")
        break
    
