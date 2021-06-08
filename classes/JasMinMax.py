from classes.Connect4 import Connect4
from json import loads, dumps
from itertools import cycle


class Jasminmax:
    
    def __init__(self, data_fp: str = "data/tree.json"):
        self.data_fp = data_fp
        self.tree = loads(open(data_fp, "r").read())
        self.pos = None
        self.branches = list(self.tree.keys())
        self.results = list(self.tree.values())
        self.branch = ""
        self.result = 0
        
        
    def navigate(self, node: str) -> None:
        self.branch += node
        
        
    def simulate_branch(self, branch: str) -> list:
        sim = Connect4()
        index = 1
        
        if branch[0] == "H":
            players = ["H", "C"]
        else:
            players = ["C", "H"]
            
        for player in cycle(players):
            try:
                sim.place_token(player, int(branch[index]))
                index += 1
            except IndexError:
                break
            
        slots = sim.slots
        slots = [el for sub in slots for el in sub]
            
        return "".join(slots) 
            
        
        
    def get_minmax(self) -> list:
        
        minmax = {i: [0, 0, 0] for i in range(7)}
        
        if self.pos is None:
            self.pos = []
            game_status = self.simulate_branch(self.branch)
            r_game_status = game_status.replace("H", "X")
            r_game_status = r_game_status.replace("C", "H")
            r_game_status = r_game_status.replace("X", "C")
            for el in self.tree.items():
                branch_status = self.simulate_branch(el[0][:len(self.branch)])
                if  branch_status == game_status:
                    self.pos.append(el)
                elif branch_status == r_game_status:
                    self.pos.append((el[0], -el[1]))
                
        else:
            old_pos = self.pos
            self.pos = []
            game_status = self.simulate_branch(self.branch)
            r_game_status = game_status.replace("H", "X")
            r_game_status = r_game_status.replace("C", "H")
            r_game_status = r_game_status.replace("X", "C")
            for el in old_pos:
                branch_status = self.simulate_branch(el[0][:len(self.branch)])
                if branch_status == game_status or branch_status == r_game_status:
                    self.pos.append(el)

           
        for el in self.pos:
            if el[1] == 1:                                      # win
                minmax[int(el[0][len(self.branch)])][0] += 1
            elif el[1] == 0:                                    # tie
                minmax[int(el[0][len(self.branch)])][1] += 1
            else:                                               # lose
                minmax[int(el[0][len(self.branch)])][2] += 1                            
                
        minmax = [(el[0], el[1][0]/(sum(el[1])+1) - el[1][2]/(sum(el[1])+1)) for el in minmax.items()]                   
        scores = list(set([el[1] for el in minmax]))
        scores = dict.fromkeys(sorted(scores, reverse=True))
        
        for el in minmax:
            if scores[el[1]] is None:
                scores[el[1]] = []
            scores[el[1]].append(el[0])    
        
        minmax = sorted(list(scores.items()), key=lambda el: el[0], reverse=True)
        return minmax
            
        
    def save_branch(self, result: int) -> None:
        self.result = result
        self.tree[self.branch] = result
        
        
    def reset_branch(self) -> None:
        self.branch = ""
        self.pos = None
        
        
    def save_data(self) -> None:
        f = open(self.data_fp, "w")
        f.write(dumps(self.tree, indent=3))
        f.close()