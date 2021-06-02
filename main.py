from classes.Connect4 import Connect4
from classes.JasMinMax import JasMinMax
from random import randint, sample
from itertools import cycle

game = Connect4()
bot = JasMinMax()
players = ["H", "C"]
players = sample(players, 2)
game_id = players[0]

print(game)

for turn in cycle(players):
    
    if turn == "H":
        while True:
            user_input = int(input("Column num. > "))
            try:
                game.place_token("H", user_input-1)
                game_id += str(user_input-1)
                break
            except Exception:
                pass        
            
    else:
        while True:
            random_col = randint(0, 6)
            try:
                game.place_token("C", random_col)
                game_id += str(random_col)
                break
            except Exception:
                pass
    
    print(game)
    
    if game.check_win("H"):
        print("HUMAN won !")
        result = -1
        break
    elif game.check_win("C"):
        print("COMPUTER won !")
        result = 1
        break
    elif game.is_full():
        print("TIE !")
        result = 0
        break


bot.add_branch(game_id, result)
bot.save_data()
game.reset_grid()

print(f"{game_id}:{result} run saved !")
                    
        
    