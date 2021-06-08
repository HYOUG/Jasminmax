from random import randint, sample, choice
from time import time, strftime, localtime, sleep
from itertools import cycle
from sys import path
from os import chdir, getcwd

chdir("..")
path.append(getcwd())

from classes.Connect4 import Connect4
from classes.Jasminmax import Jasminmax
from utils.misc import get_branches_num


train_time = int(input("Training time (secs.) : "))
print(f"Training for {train_time} secs.: ", end="")
print(f"{strftime('%H:%M:%S')} => {strftime('%H:%M:%S', localtime(time() + train_time))}")


game = Connect4()
ai = Jasminmax()
start_time = time()
game_num = 0

while (time() - start_time) <= train_time:
    
    players = sample(["H", "C"], 2)
    branch = players[0]
    ai.navigate(players[0])

    for turn in cycle(players):                                           # one game
        
        if turn == "H":                                                   # fake human's turn
            minmax = ai.get_minmax()
            #print(minmax)
            for score in minmax:
                for pos in range(len(score[1])):
                    try:
                        max_branch = choice(score[1])
                        game.place_token(turn, max_branch)
                        break
                    except Exception:
                        pass
            ai.navigate(str(max_branch))

                
        else:                                                             # computer's turn
            minmax = ai.get_minmax()
            #print(minmax)
            for score in minmax:
                for pos in range(len(score[1])):
                    try:
                        max_branch = choice(score[1])
                        game.place_token(turn, max_branch)
                        break
                    except Exception:
                        pass
            ai.navigate(str(max_branch))
            
        #print(game)
        #sleep(0.5)        
        
        if game.check_win(turn):
            #print(f"{turn} won !")
            if turn == "H":
                result = -1
            elif turn == "C":
                result = 1
            break

        elif game.is_full():
            #print("TIE !")
            result = 0
            break
        
    #print(f"{ai.branch}:{result}")
    ai.save_branch(result)
    ai.save_data()
    
    ai.reset_branch()
    game.reset_grid()
    
    game_num += 1
    


    
print(f"Training finished : +{game_num} games simulated")
print(f"Simulating rate : {int(game_num / train_time)} games simulated / secs.")
print(f"Total games simulated : {get_branches_num()}")