from classes.Connect4 import Connect4
from classes.Jasminmax import Jasminmax
from utils.misc import get_stats
from random import sample, choice
from itertools import cycle

game = Connect4()
ai = Jasminmax()
players = sample(["H", "C"], 2)
branch = players[0]
ai.navigate(players[0])
stats = get_stats()

print("="*50)
print(f"Number of branches : {stats['branches_num']}")
print(f"Number of Wins : {stats['wins_num']}")
print(f"Number of Loses : {stats['loses_num']}")
print(f"Number of Ties : {stats['ties_num']}")
print(f"Average branch lenght : {stats['average_branch_len']}")
print("="*50)

print(game)

for turn in cycle(players):
    
    if turn == "H":
        while True:
            user_input = int(input("Column num. > "))
            try:
                game.place_token(turn, user_input-1)
                ai.navigate(str(user_input-1))
                break
            except Exception:
                pass        
            
    else:
        minmax = ai.get_minmax()
        
        print("-"*60)
        print(f"Branch : {ai.branch} ({len(ai.pos)} matches)")
        print(f"Minmax : {minmax}")
        print(f"Max : {minmax[0]}")
        print("-"*60)

        for score in minmax:
            for pos in range(len(score[1])):
                try:
                    max_branch = choice(score[1])
                    game.place_token(turn, max_branch)
                    break
                except Exception:
                    pass
            break
        ai.navigate(str(max_branch))

                
    print(game)
    
    if game.check_win(turn):
        print(f"{turn} won !")
        if turn == "H":
            result = -1
        elif turn == "C":
            result = 1
        break

    elif game.is_full():
        print("tie !")
        result = 0
        break


ai.save_branch(result)
ai.save_data()
game.reset_grid()

print(f"{ai.branch}:{ai.result} run saved !")
                    
        
    