from json import loads, dumps

class JasMinMax:
    
    def __init__(self):
        self.data = loads(open("data/tree.json", "r").read())
        self.paths = self.data.keys()
        self.results = self.data.values()
        self.path = []
        self.result = 0
        
    def nav(self, node: str) -> None:
        self.path.append(node)
        
    def get_minmax(self) -> list:
        pos = {el:self.data[el] for el in self.paths if el.startswith("".join(self.path))}
        minmax = {}
        for el in pos.items():
            if el[0].split(".")[len(self.path)] in minmax:
                minmax[el.split(".")[len(self.path)]] = el[1]
            else:
                minmax[el.split(".")[len(self.path)]] += el[1]
        return minmax.items().sort(key=lambda el: el[1])
            
 
    def save_branch(self, outcome: str) -> None:
        self.result = outcome
        
    def add_branch(self, game_id: str, result: int) -> None:
        self.data[game_id] = result
        
    def save_data(self) -> None:
        f = open("data/tree.json", "w")
        f.write(dumps(self.data, indent=3))
        f.close()