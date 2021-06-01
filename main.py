from classes.Connect4 import Connect4
from classes.JasMinMax import JasMinMax
from random import randint

game = Connect4()
bot = JasMinMax()
players = ["H", "C"]


for i in range(1000):
    print(i)
    
    turn = players[randint(0, 1)]
    game_id = turn

    #print(game)

    while True:                 # one game
        
        if turn == "H":
            while True:
                # user_input = int(input("Column num. > "))
                # try:
                #     game.place_token("H", user_input-1)
                #     game_id += str(user_input-1)
                #     break
                # except Exception:
                #     pass        
                random_col = randint(0, 6)          # fake ooman
                try:
                    game.place_token("H", random_col)
                    game_id += str(random_col)
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
        
        #print(game)
        
        if game.check_win("H"):
            #print("H won !")
            result = -1
            break
        elif game.check_win("C"):
            #print("C won !")
            result = 1
            break
        elif game.is_full():
            #print("tie !")
            result = 0
            break
        
        if turn == "H":
            turn = "C"
        else:
            turn = "H"

    bot.add_branch(game_id, result)
    bot.save_data()
    
    game.reset_grid()

    #print(f"{'.'.join(game_id)}:{result} run saved !")
        
    #print("end.")
                    
        
    