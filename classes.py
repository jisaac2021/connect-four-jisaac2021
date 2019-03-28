
import string

class Chip:

    def __init__(self, color):
        self.color = color


class Player:

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def play_chip(self):
        return Chip(self.color)


class Display:

    def __init__(self):
        pass

    def draw(self):
        pass


class ConnectFour:


    def __init__(self, player_1, player_2, rows, cols):
        self.player_1 = player_1
        self.player_2 = player_2
        self.num_rows = rows
        self.num_cols = cols

        self.num_turns = 0

        self.board = {}
        for i in range(self.num_cols):
            label = string.ascii_uppercase[i]
            self.board[label] = []
            print(self.board)

    def play_turn(self):

        if self.num_turns % 2 == 0:
            player = self.player_1
        else:
            player = self.player_2

        print('%s, it is your turn' % player.name)
        col = input('Choose a column: ')

        if len(self.board[col]) == self.num_rows:
            print('Column %s is full!' % col)
            return False
        else:
            self.board[col].append(player.play_chip())
            self.num_turns += 1
            return True

    def show_state(self):
        print(self.board)

    def check_win(self):
        pass
