from itertools import permutations
from modules.utils import remove_duplicates


class Connect4:
    
    def __init__(self):
        self.slots = [["_" for _ in range(6)] for _ in range(7)]
        
        
    def set_grid(self) -> None:
       self.grid = "="*29 + "\n" + "".join(["".join([f"| {self.slots[col][row]} " for col in range(7)]) + "|\n" for row in range(5, -1, -1)]) + "="*29
       
       
    def reset_grid(self) -> None:
        self.slots = [["_" for _ in range(6)] for _ in range(7)]
        
        
    def place(self, char: str, col: int) -> None:
        try:
            self.slots[col][self.slots[col].index("_")] = char
        except ValueError:
            raise Exception(f"Impossible Move : Column number {col} is full")
        
        
    def get_alignments(self, char_list: list) -> int:
        targets = list(map(lambda el: list(el) , permutations(char_list, len(char_list))))
        #targets = remove_duplicates(targets) <- fix that (remove dupes)
        targets_len = len(char_list)
        alignments = 0
        
        ver_pos = []
        hor_pos = []
        dia_pos = []
        
        for col in range(7):
            for row in range(6-(targets_len-1)):
                ver_pos.append([self.slots[col][row + i] for i in range(targets_len)])
                
        for col in range(7-(targets_len-1)):
            for row in range(6):
                hor_pos.append([self.slots[col + i][row] for i in range(targets_len)])
        
        for col in range(7-(targets_len-1)):
            for row in range(6-(targets_len-1)):
                dia_pos.append([self.slots[col + i][row + i] for i in range(targets_len)])
        for col in range(7-(targets_len-1)):
            for row in range(0+(targets_len-1), 6):
                dia_pos.append([self.slots[col + i][row - i] for i in range(targets_len)])
                
        pos = ver_pos + hor_pos + dia_pos  
        alignments = sum([pos.count(target) for target in targets])
        
        return alignments
    
    
    def check_win(self, char: str) -> bool:
        alignments = self.get_alignments([char] * 4)
        return alignments >= 1
            
            
    def is_full(self) -> bool:
        return sum([col.count("_") for col in self.slots]) == 0
        
        
    def __str__(self) -> str:
        self.set_grid()
        return self.grid