
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
        pass


    def play_turn(self):
        pass

    def show_state(self):
        pass
