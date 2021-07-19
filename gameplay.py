win_combinations = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

def display_board(board):
    print("{}  |  {}  |  {} ".format(board[0], board[1], board[2]))
    print("-------------")
    print("{}  |  {}  |  {} ".format(board[3], board[4], board[5]))
    print("-------------")
    print("{}  |  {}  |  {} ".format(board[6], board[7], board[8]))

def input_to_index(user_input):
    return user_input - 1

def move(board, index, player):
    board[index] = player

def is_position_taken(board, index):
    if (board[index] or board[index] == " "):
        return True

def is_valid_move(board, index):
    if index.range(0,8) and is_position_taken(board, index) == True:
        return True

def turn(board):
    player_input = input("Please enter 1-9: ")
    index = input_to_index(player_input)
    if is_valid_move(board, index):
        move(board, index, current_player(board))
        display_board(board)
    else:
        turn(board)

def turn_count(board):
    turns = 0
    for player in board:
        if player == "X" or player == "O":
            turns += 1
    return turns

def current_player(board):
    if turn_count(board) % 2 == 0:
        return "X"
    else:
        return "O"

def is_won(board):
    for index in win_combinations:
        board[index[0]] == board[index[1]] and board[index[1]] == board[index[2]] and is_position_taken(board, index[0])

def is_full(board):
    if " " not in board:
        return True

def is_draw(board):
    is_full(board) and not is_won(board)

def is_over(board):
    is_won(board) or is_draw(board)

def winner(board):
    winning_move = []
    if winning_move == is_won(board):
        board[winning_move[0]]

def play(board):
    while not is_over(board):
        turn(board)
    if is_won(board):
        print("Congratulations {}!".format(winner(board)))
    elif is_draw(board):
        print("Cat's Game!")
