from random import randint, sample
from time import time
from itertools import cycle
from sys import path
from os import chdir, getcwd

chdir("..")
path.append(getcwd())

from classes.Connect4 import Connect4
from classes.JasMinMax import JasMinMax

game = Connect4()
bot = JasMinMax()
players = ["H", "C"]
start = time()
training_time = int(input("Training time : "))


while (time() - start) <= training_time:
    
    print(f"time left : {training_time - (int(time()) - int(start))}")
    players = sample(players, 2)
    game_id = players[0]

    for turn in cycle(sample(players, 2)):                                # one game
        
        if turn == "H":                                                   # fake human's turn
            while True:       
                random_col = randint(0, 6)
                try:
                    game.place_token("H", random_col)
                    game_id += str(random_col)
                    break
                except Exception:
                    pass
                
        else:                                                             # computer's turn
            while True:
                random_col = randint(0, 6)
                try:
                    game.place_token("C", random_col)
                    game_id += str(random_col)
                    break
                except Exception:
                    pass
        
        if game.check_win("H"):
            result = -1
            break
        elif game.check_win("C"):
            result = 1
            break
        elif game.is_full():
            result = 0
            break

    bot.add_branch(game_id, result)
    bot.save_data()
    game.reset_grid()
                    
        
    