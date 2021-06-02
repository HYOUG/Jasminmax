from json import loads, dumps
from utils.functions import split_str

class JasMinMax:
    
    def __init__(self):
        self.tree = loads(open("data/tree.json", "r").read())
        self.branches = list(self.tree.keys())
        self.results = list(self.tree.values())
        self.branch = ""
        self.result = 0
        
    def navigate(self, node: str) -> None:
        self.branch += node
        
    def get_minmax(self) -> list:
        pos = [el for el in self.tree.items() if el[0].startswith(self.branch)]
        minmax = {}
        for el in pos:
            if el[0][len(self.branch)] not in minmax:
                minmax[el[0][len(self.branch)]] = el[1]
            else:
                minmax[el[0][len(self.branch)]] += el[1]
        return list(minmax.items()).sort(key=lambda el: el[1])
            
 
    def set_outcome(self, outcome: str) -> None:
        self.result = outcome
        
    def add_branch(self, branch: str, result: int) -> None:
        self.tree[branch] = result
        
    def save_data(self) -> None:
        f = open("data/tree.json", "w")
        f.write(dumps(self.tree, indent=3))
        f.close()