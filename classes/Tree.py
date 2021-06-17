class Node:
    
    def __init__(self, name = None, value = None, player = None, parent = None) -> None:
        self.name = name
        self.value = value
        self.player = player
        self.parent = parent
        self.childs = []
        
        if parent is not None:
            parent.add_child(self)
            self.depth = parent.depth + 1
        else:
            self.depth = 0       
        
        
    def add_child(self, child):
        self.childs.append(child)
        child.parent = self
        
        
    def childs_values(self) -> list:
        return [child.value for child in self.childs]
    
    
    def __repr__(self) -> str:
        return f"<Node | name: {self.name} |  value: {self.value}>"
             
             
    def __str__(self, level = 0) -> str:
        display = "\t" * level + repr(self) + "\n"
        for child in self.childs:
            display += child.__str__(level + 1)
        return display



class Tree:
    
    def __init__(self) -> None:
        self.nodes = []
        
        
    def add_node(self, name = None, value = None, player= None, parent = None) -> Node:
        new_node = Node(name, value, player, parent)
        self.nodes.append(new_node)
        return new_node
        
        
    def get_nodes_by_depth(self, depth) -> list:
        selection = []
        for node in self.nodes:
            if node.depth == depth:
                selection.append(node)
        return selection 
    
    
    def __str__(self) -> str:
        o = self.get_nodes_by_depth(0)[0]
        return str(o)
            
