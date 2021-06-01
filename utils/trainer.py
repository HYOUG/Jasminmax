from classes.Connect4 import Connect4
from classes.JasMinMax import JasMinMax
from random import randint
from time import time
from itertools import cycle

game = Connect4()
bot = JasMinMax()

players = cycle(["H", "C"])
start = time()
training_time = float(input("Training time : "))


while (time() - start) <= training_time:
    print(f"time left : {training_time - (time() - start)}")
    
    turn = players[randint(0, 1)]
    game_id = turn

    while True:                                                           # one game
        
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
        
        turn = next(players)

    bot.add_branch(game_id, result)
    bot.save_data()
    game.reset_grid()
                    
        
    