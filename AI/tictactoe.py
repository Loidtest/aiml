from random import choice
win_combinations = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

ai_sign = 'X'
opp_sign = 'O'
empty = '.'
board = list(empty * 9)
game_ended = False
empty_cell = 9

def print_board():
    print(" ")
    print("\t".join(board[:3]))
    print("\t".join(board[3:6]))
    print("\t".join(board[6:]))
    print(" ")
def opp_move(row,col):
    index = 3*(row-1)+(col-1)
    if(board[index] == empty):
        board[index] = opp_sign
        return True
    else:
        return False
def check_win(sign):
    for x in win_combinations:
        if(board[x[0]] == sign and board[x[1]] == sign and board[x[2]] == sign):
            return True
    return False

def all_available_moves():
    moves = []
    for i,v in enumerate(board):
        if(v == empty):
            moves.append(board[:i]+list(ai_sign)+board[i+1:])
    return moves
def ai_move():
    return choice(all_available_moves())

if __name__ == '__main__':
    while empty_cell > 0 and not(game_ended):
        if(empty_cell % 2 == 0):
            board = ai_move()
            print_board()
            if(check_win(ai_sign)):
                    print("AI has won the game")
                    break
            empty_cell -=1
        else:
            row = int(input("enter the row : "))
            col = int(input("enter the col : "))
            if(opp_move(row,col)):
                print_board()
                if(check_win(opp_sign)):
                    print("user has won the game")
                    break
            else:
                print("Wrong position! EXIT ... ")
                break
            empty_cell -=1