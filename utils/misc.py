from json import loads, dumps


def get_stats() -> dict:
    stats = {}
    f = open("data/tree.json", "r")
    data = loads(f.read())
    
    stats["branches_num"] = len(data.keys())
    stats["wins_num"] = len(list(filter(lambda el: el[1] == 1, list(data.items()))))
    stats["loses_num"] = len(list(filter(lambda el: el[1] == -1, list(data.items()))))
    stats["ties_num"] = len(list(filter(lambda el: el[1] == 0, list(data.items()))))
    stats["average_branch_len"] = sum([len(el[0]) for el in data.items()]) / len(data.keys())
    
    
def duplicate_data(filename: str) -> None:
    f1 = open("data/tree.json", "r")
    f2 = open(f"data/{filename}.json", "w")
    
    data = loads(f1.read())
    f2.write(dumps(data, indent=3))
    
    f1.close()
    f2.close()


def wipe_data() -> None:
    f = open("data/tree.json", "w")
    f.close()