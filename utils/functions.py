from json import loads, dumps

def get_data_stats():
    f = open("data/tree.json", "r")
    data = loads(f.read())
    keys = list(data.keys())
    print(f"Number of branches : {len(keys)}")

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
    
def split_str(string: str) -> list:
    return [char for char in string]


get_data_stats()