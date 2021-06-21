from classes.Connect4 import Connect4
from classes.Tree import Tree, Node
from modules.utils import *
from itertools import cycle
from math import inf


def get_score(state: str) -> int or bool:
    """Evaluate the given state as a state"""
    sim = Connect4()
    index = 1
    
    if state.startswith("H"):
        players = ["H", "C"]
    else:
        players = ["C", "H"]
        
    for player in cycle(players):
        sim.place(player, int(state[index]))
        
        if sim.check_win(player):
            if player == "H":
                return -inf
            elif player == "C":
                return inf
            
        elif index == len(state) - 1:
            break
        
        index += 1
            
    h_1_combo = sim.get_alignments(["H"] * 1 + ["_"] * 3) * -1
    h_2_combo = sim.get_alignments(["H"] * 2 + ["_"] * 2) * -10
    h_3_combo = sim.get_alignments(["H"] * 3 + ["_"] * 1) * -100
    c_1_combo = sim.get_alignments(["C"] * 1 + ["_"] * 3) * 1
    c_2_combo = sim.get_alignments(["C"] * 2 + ["_"] * 2) * 10
    c_3_combo = sim.get_alignments(["C"] * 3 + ["_"] * 1) * 100

    return sum([h_1_combo, h_2_combo, h_3_combo, c_1_combo, c_2_combo, c_3_combo])


def gen_tree(state: str, depth: int) -> Tree:
    """Generate a tree of the given depth from the whose origin is the given state"""
    t = Tree()
    t.add_node(state)
    
    for depth_level in range(depth):
        for node in t.get_nodes_by_depth(depth_level):
            for pos in [pos for pos in range(7) if is_legal(f"{node.name}{pos}")]:
                t.add_node(name=f"{node.name}{pos}", parent=node)
                    
    return t
                
                
def calc_minimax(node: Node, tree: Tree, depth: int, max_player: bool) -> int:
    """Calculate the minimax path recursively from the given node, tree, depth and max player"""
    if depth == 0 or node in tree.get_nodes_by_depth(tree.get_nodes_by_depth):
        node.value = get_score(node.name)
        return get_score(node.name)
    elif max_player:
        max_value = -inf
        for child in node.childs:
            max_value = max(max_value, calc_minimax(child, tree, depth-1, False))
        node.value = max_value
        return max_value    
    else:
        min_value = inf
        for child in node.childs:
            min_value = min(min_value, calc_minimax(child, tree, depth-1, True))
            node.value = min_value
        return min_value
                  

def get_minimax(state: str, depth: int) -> int:
    """Return the best choice according to the minimax algorithm"""
    t = gen_tree(state, depth)      
    o = t.get_nodes_by_depth(0)[0]
    pos = t.get_nodes_by_depth(1)
    
    calc_minimax(o, t, depth, True)
    
    best_pos = max(pos, key=lambda node: node.value)
    
    return int(best_pos.name[len(state)])
