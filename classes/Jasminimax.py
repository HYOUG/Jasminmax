from classes.Connect4 import Connect4
from classes.Tree import Tree, Node
from modules.utils import *
from itertools import cycle
from math import inf


class Jasminimax:
    
    def __init__(self):
        self.branch = ""
        
        
    def navigate(self, node: str) -> None:
        self.branch += node
        
        
    def eval_branch(self, branch: str, player: str = "C") -> int or bool:
        sim = Connect4()
        index = 1
        
        if branch.startswith("H"):
            players = ["H", "C"]
        else:
            players = ["C", "H"]
            
        for player in cycle(players):
            try:
                sim.place(player, int(branch[index]))
            except Exception:
                return False
            
            if sim.check_win(player):
                if player == "H":
                    return -1*10**9
                elif player == "C":
                    return 1*10**9
                
            elif index == len(branch) - 1:
                break
            
            index += 1
                
        if player == "C":
            h_1_combo = sim.get_alignments(["H"] * 1 + ["_"] * 3) * -1
            h_2_combo = sim.get_alignments(["H"] * 2 + ["_"] * 2) * -10
            h_3_combo = sim.get_alignments(["H"] * 3 + ["_"] * 1) * -100
            c_1_combo = sim.get_alignments(["C"] * 1 + ["_"] * 3) * 1
            c_2_combo = sim.get_alignments(["C"] * 2 + ["_"] * 2) * 10
            c_3_combo = sim.get_alignments(["C"] * 3 + ["_"] * 1) * 100

            
        elif player == "H":
            h_1_combo = sim.get_alignments(["H"] * 1 + ["_"] * 3) * 1
            h_2_combo = sim.get_alignments(["H"] * 2 + ["_"] * 2) * 10
            h_3_combo = sim.get_alignments(["H"] * 3 + ["_"] * 1) * 100
            c_1_combo = sim.get_alignments(["C"] * 1 + ["_"] * 3) * -1
            c_2_combo = sim.get_alignments(["C"] * 2 + ["_"] * 2) * -10
            c_3_combo = sim.get_alignments(["C"] * 3 + ["_"] * 1) * -100
        
        return sum([h_1_combo, h_2_combo, h_3_combo, c_1_combo, c_2_combo, c_3_combo])
            
        
    def get_minimax(self, depth: int, player: str = "C") -> dict:
        t = Tree()
        t.add_node(self.branch, player=player)
          
        for depth_level in range(depth):
            for node in t.get_nodes_by_depth(depth_level):
                for pos in range(7):
                    if node.player == "H":
                        node_player = "C"
                    else:
                        node_player = "H"
                    t.add_node(name=node.name + str(pos), player=node_player, parent=node)          
        
        for end_node in t.get_nodes_by_depth(depth):
            end_node.value = self.eval_branch(end_node.name, player)      
        
        for depth_level in range(depth-1, 0, -1):         
            parent_nodes = t.get_nodes_by_depth(depth_level)                    
            for parent in parent_nodes:
                pos = list(filter(lambda el: el is not False, parent.childs_values()))
                if pos:
                    if parent.player == player:
                        parent.value = max(pos)
                    else:
                        parent.value = min(pos)
                else:
                    parent.value = False
                    
        o = t.get_nodes_by_depth(0)[0]
        pos = list(filter(lambda el: el.value is not False, o.childs))
        best_pos = max(pos, key=lambda el: el.value)
                                  
        return int(best_pos.name[len(self.branch)])
    
        
    def save_branch(self, result: int) -> None:
        self.result = result
        self.tree[self.branch] = result
        
        
    def reset_branch(self) -> None:
        self.branch = ""
        self.pos = None