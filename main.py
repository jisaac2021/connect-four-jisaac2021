"""
Main game loop
"""

from classes import Player, ConnectFour

p1 = Player('red', 'shlomo')
p2 = Player('black', 'shlomit')

game = ConnectFour(p1, p2, 6, 7)

while True:

    game.show_state()
    game.play_turn()
    game.check_win()
