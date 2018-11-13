names = []

def addName(name,amount):
    for i in range(amount):
        names.append(name)

addName("PERCENTAGE_DONE",1)
addName("LOCAL", 16)
addName("HIGHEST_HALITE",48)
addName("CLOSEST_DROP_OFF",4)
addName("LOCAL_AREA",4)
addName("CURRENT_CELL",5)

print(names)
