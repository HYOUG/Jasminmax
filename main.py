from classes.Connect4 import Connect4
from classes.Jasminimax import Jasminimax
from random import sample
from itertools import cycle

game = Connect4()
ai = Jasminimax()
players = sample(["H", "C"], 2)
players_names = {"H": "Human", "C": "Computer"}
branch = players[0]
ai.navigate(players[0])


print(game)

for player in cycle(players):
    
    if player == "H":
        while True:
            user_input = int(input("Your turn : "))
            try:
                game.place(player, user_input-1)
                ai.navigate(str(user_input-1))
                break
            except Exception:
                pass        
            
    else:
        minimax = ai.get_minimax(4)
        print(f"Computer's turn : {minimax + 1}")
        game.place(player, minimax)
        ai.navigate(str(minimax))
        
        
    print(game)
    
    
    if game.check_win(player):
        print(f"{players_names[player]} won !")
        break

    elif game.is_full():
        print("tie !")
        break    