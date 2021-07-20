

class Play_Game:
    def __init__(self):
        self.board = ["0","1","2","3","4","5","6","7","8"]
        self.empty = [0,1,2,3,4,5,6,7,8]
        self.win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
            ]

    def display_board(self, board):
        print("\n")
        print("{}  |  {}  |  {} ".format(board[0], board[1], board[2]))
        print("-------------")
        print("{}  |  {}  |  {} ".format(board[3], board[4], board[5]))
        print("-------------")
        print("{}  |  {}  |  {} ".format(board[6], board[7], board[8]))

    def player_input(self, player, board):
        symbol = ['X', 'O']
        correct_input = True

        position = int(input('player {playerNo}, choose field for {symbol}\n'.format(playerNo=player+1, symbol=symbol[player])))

        if board[position] == 'X' or board[position] == 'O':
            correct_input = False
        
        if not correct_input:
            print("Position already taken!")
            self.display_board(board)
            self.player_input(player, board)
        else:
            self.empty.remove(position)
            board[position] = symbol[player]
            return 1

    def check_win(self, board):
        player_symbol = ['X', 'O']
        for check in self.win_combinations:
            first = board[check[0]]
            if first != ' ':
                won = True
                for point in check:
                    if board[point] != first:
                        won = False
                        break
                if won:
                    if first == player_symbol[0]:
                        self.display_board(board)
                        print('Player 1 wins!')
                    else:
                        self.display_board(board)
                        print('Player 2 wins!')
                    break
            else:
                won = False
        if won:
            return 0
        else:
            return 1


    def play(self):
        player = 0
        while self.empty and self.check_win(self.board):
            self.display_board(self.board)
            print("\n")
            self.player_input(player, self.board)
            player = int(not player)
        if not self.empty:
            self.display_board(self.board)
            print("Cat's Game!")
