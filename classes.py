
import string

class Chip:

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color


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

    def play_turn(self):
        global player
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
        # display column names
        header = ''
        for k in self.board.keys():
            header += k
        print(header)

        # display column contents
        for i in range(self.num_rows):
            row_to_show = ''
            for k in self.board.keys():
                if len(self.board[k]) >= self.num_rows - i:
                    chip = self.board[k][self.num_rows - i - 1]
                    row_to_show += chip.color[0] # show 'r' or 'b'
                else:
                    row_to_show += ' '

            print(row_to_show)

    def check_win(self):

        for k in self.board: # check for vertical win
            acc = 0
            for c in self.board[k]:
                if c.color == player.color:
                    acc +=1
                if acc == 4:
                    print('Connect Four!')
                    return True

            return False
