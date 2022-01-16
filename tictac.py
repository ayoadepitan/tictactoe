import random


class TicTacToe:
    def __init__(self):
        self.board = []

    def createBoard(self):
        for y in range(3):
            row = []
            for x in range(3):
                row.append('-')
            self.board.append(row)
        print(self.board)

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        else:
            return True

    def checkWinner(self, player):
        # Check rows
        win = None
        boardLen = len(self.board)
        for i in range(boardLen):
            win = True
            for j in range(boardLen):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # Check columns
        for i in range(boardLen):
            win = True
            for j in range(boardLen):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # Check diagnonal
        win = True
        for i in range(boardLen):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(boardLen):
            if self.board[i][boardLen - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.createBoard()

        player = 'X' if random.randrange(0, 2) == 1 else 'O'

        while True:
            print(f'Player {player} turn')
            self.show_board()
            row, col = list(
                map(int, input("Enter row and column numbers to mark spot: ").split()))

            self.board[row][col] = player
            if self.checkWinner(player):
                print(f'Player {player} won!')
                break

            if self.is_board_filled():
                print('It\'s a tie!')
                break

            player = 'X' if player == 'O' else 'O'

        self.show_board()


tictac = TicTacToe()
tictac.start()
