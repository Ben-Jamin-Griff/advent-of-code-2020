## Part 1

# Opening the input
f = open("./data/day7data.txt","r")
lines=f.readlines()
data = []
for val in lines:
    data.append(val.rstrip())

bagList = {}
for rule in data:
    mainSubBags = rule.split("contain", 1)
    key = mainSubBags[0].rstrip()
    subBags = mainSubBags[1].split(",")
    subDict = {}
    for bag in subBags:
        bag = bag.rstrip()
        bag = bag.replace('.','')
        if 'no other bags' in bag:
            valueForDict = None
            subDict = valueForDict
        else:
            bagData = bag.split(" ", 2)
            subKey = bagData[2]
            subValue = int(bagData[1])
            subDict[subKey] = subValue
    bagList[key] = subDict

print(bagList)
    