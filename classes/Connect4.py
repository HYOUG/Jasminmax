class Connect4:
    
    def __init__(self):
        self.slots = [["_" for _ in range(6)] for _ in range(7)]
        self.grid = "="*29 + "\n" + "".join(["".join([f"| {self.slots[col][row]} " for col in range(7)]) + "|\n" for row in range(5, -1, -1)]) + "="*29
        
        
    def set_grid(self) -> None:
       self.grid = "="*29 + "\n" + "".join(["".join([f"| {self.slots[col][row]} " for col in range(7)]) + "|\n" for row in range(5, -1, -1)]) + "="*29
       
       
    def reset_grid(self) -> None:
        self.slots = [["_" for _ in range(6)] for _ in range(7)]
        self.set_grid()
        
        
    def place_token(self, char: str, col: int) -> None:
        try:
            self.slots[col][self.slots[col].index("_")] = char
            self.set_grid()
        except ValueError:
            raise Exception(f"column num. {col} is full")
        
        
    def check_win(self, char: str) -> bool:
        target = [char] * 4
        ver_pos = []
        hor_pos = []
        dia_pos = []
        
        for col in range(7):
            for row in range(6-3):
                ver_pos.append([self.slots[col][row + i] for i in range(4)])
                
        for col in range(7-3):
            for row in range(6):
                hor_pos.append([self.slots[col + i][row] for i in range(4)])
        
        for col in range(7-3):
            for row in range(6-3):
                dia_pos.append([self.slots[col + i][row + i] for i in range(4)])
        for col in range(0+3, 7):
            for row in range(0+3, 6):
                dia_pos.append([self.slots[col - i][row - i] for i in range(4)])
                       
        if target in ver_pos:
            return True
        if target in hor_pos:
            return True
        if target in dia_pos:
            return True
        return False
            
            
    def is_full(self) -> bool:
        return sum([col.count("_") for col in self.slots]) == 0
        
        
    def __str__(self) -> str:
        return self.grid