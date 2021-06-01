from json import loads, dumps

def wipe_data() -> None:
    f = open("data/tree.json", "w")
    f.close()
    
def duplicate_data(filename: str) -> None:
    f1 = open("data/tree.json", "r")
    f2 = open(f"data/{filename}.json", "w")
    
    data = loads(f1.read())
    f2.write(dumps(data, indent=3))
    
    f1.close()
    f2.close()