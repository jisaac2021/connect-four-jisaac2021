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

        for k in self.board.keys(): # check for vertical win

            if len(self.board[k]) > 0:
                chip = self.board[k][0].color
                streak = 1

                for c in self.board[k][1:]:

                    if chip == player.color:
                        streak += 1
                        print(streak)
                    else:
                        streak = 1
                        chip = c

                    if streak == 4:
                        print('Connect Four!')
                        print('%s has won the game.' % player.name)
                        return True

        for row in range(self.num_rows):  # check for horizantal win
            prev_chip = None

            for k in self.board.keys():

                if len(self.board[k]) > row:
                    chip = self.board[k][row].color

                    if chip == prev_chip:
                        streak += 1
                        print(streak)

                    else:
                        streak = 1
                        prev_chip = chip

                if streak == 4:
                    print('Connect Four!')
                    print('%s has won the game.' % player.name)
                    return True

        for k in self.board.keys(): # check for diagonal win
            prev_chip = None

            for row in range(self.num_rows):

                if len(self.board[k]) > row:
                    chip = self.board[k][row].color
                    print(chip)
                    streak = 1

                    if chip == prev_chip:
                        streak += 1

                    else:
                        streak = 1
                        prev_chip = chip

            if streak == 4:
                print('Connect Four!')
                print('%s has won the game.' % player.name)
                return True
