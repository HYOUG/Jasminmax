from random import randint, sample
from time import time
from itertools import cycle
from sys import path
from os import chdir, getcwd
from multiprocessing import Pool

chdir("..")
path.append(getcwd())

from classes.Connect4 import Connect4
from classes.JasMinMax import JasMinMax
from utils.functions import get_branches_num

game = Connect4()
bot = JasMinMax()
players = ["H", "C"]
start = time()
i = 0

train_time = int(input("Training time (secs.) : "))
print(f"Training J4sMinMax for {train_time} seconds...")


while (time() - start) <= train_time:
    
    players = sample(players, 2)
    branch = players[0]

    for turn in cycle(sample(players, 2)):                                # one game
        
        if turn == "H":                                                   # fake human's turn
            while True:       
                random_col = randint(0, 6)
                try:
                    game.place_token("H", random_col)
                    branch += str(random_col)
                    break
                except Exception:
                    pass
                
        else:                                                             # computer's turn
            while True:
                random_col = randint(0, 6)
                try:
                    game.place_token("C", random_col)
                    branch += str(random_col)
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

    bot.add_branch(branch, result)
    game.reset_grid()
    i += 1
    
bot.save_data()
    
print(f"Training finished : +{i} games simulated")
print(f"Simulating rate : {i / train_time} games simulated / secs.")
print(f"Total games simulated : {get_branches_num()} games")
                    
        
    