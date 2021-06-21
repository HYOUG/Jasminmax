from classes.Connect4 import Connect4
from modules.minimax import get_minimax
from random import sample
from itertools import cycle
from time import time


game = Connect4()
players = sample(["H", "C"], 2)
players_names = {"H": "Human", "C": "Minimax AI"}
game.state += players[0]

print(game)

for player in cycle(players):
    
    if player == "H":
        while True:
            user_input = int(input("Your turn : "))
            try:
                game.place(player, user_input-1)
                break
            except Exception:
                print(f"Impossible move : {user_input}")
                pass        
            
    else:
        start = time()
        minimax = get_minimax(game.state, 4)
        print(f"Minimax time : {int(time() - start)} secs.")
        print(f"Computer's turn : {minimax + 1}")
        game.place(player, minimax)
        
        
    print(game)
    
    
    if game.check_win(player):
        print(f"{players_names[player]} won !")
        break

    elif game.is_full():
        print("Tie !")
        break