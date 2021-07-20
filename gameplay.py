win_combinations = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]
empty = [0,1,2,3,4,5,6,7,8]

def display_board(board):
    print("\n")
    print("{}  |  {}  |  {} ".format(board[0], board[1], board[2]))
    print("-------------")
    print("{}  |  {}  |  {} ".format(board[3], board[4], board[5]))
    print("-------------")
    print("{}  |  {}  |  {} ".format(board[6], board[7], board[8]))

def player_input(player, board):
    symbol = ['X', 'O']
    correct_input = True

    position = int(input('player {playerNo}, choose field for {symbol}\n'.format(playerNo=player+1, symbol=symbol[player])))

    if board[position] == 'X' or board[position] == 'O':
        correct_input = False
    
    if not correct_input:
        print("Position already taken!")
        display_board(board)
        player_input(player, board)
    else:
        empty.remove(position)
        board[position] = symbol[player]
        return 1

def check_win(board):
    player_symbol = ['X', 'O']
    for check in win_combinations:
        first = board[check[0]]
        if first != ' ':
            won = True
            for point in check:
                if board[point] != first:
                    won = False
                    break
            if won:
                if first == player_symbol[0]:
                    display_board(board)
                    print('Player 1 wins!')
                else:
                    display_board(board)
                    print('Player 2 wins!')
                break
        else:
            won = False
    if won:
        return 0
    else:
        return 1


def play(board):
    player = 0
    while empty and check_win(board):
        display_board(board)
        print("\n")
        player_input(player, board)
        player = int(not player)
    if not empty:
        display_board(board)
        print("Cat's Game!")
