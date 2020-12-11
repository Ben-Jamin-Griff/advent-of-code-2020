## Part 1

# Opening the input
f = open("./data/day7data.txt","r")
lines=f.readlines()
data = []
for val in lines:
    data.append(val.rstrip())

class Bag:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def searchBag(self):
        print('This is a ' + self.name + ' bag and it contains...')
        for key in self.children.keys():
            print( key + ' bags.')

    def updateChild(self, child, number):
        self.children[child] = number

    def isChild(self, child, bagList):
        isAChild = False
        if child in self.children.keys():
            isAChild = True
            return isAChild
        else:
            for key in self.children.keys():
                for bag in bagList:
                    if bag.name == key:
                        isAChild = bag.isChild(child, bagList)
                        if isAChild:
                            return isAChild
        return isAChild

# Creating bag list
bagList = []
for rule in data:
    mainSubBags = rule.split(" bags contain", 1)
    key = mainSubBags[0].rstrip()
    thisBag = Bag(key)
    subBags = mainSubBags[1].split(",")
    for bag in subBags:
        bag = bag.replace(' bags.','')
        bag = bag.rstrip()
        if 'no other' in bag:
            valueForDict = None
            thisBag.updateChild(bag, valueForDict)
        else:
            bagData = bag.split(" ", 2)
            subKey = bagData[2].replace(' bags', '')
            subValue = int(bagData[1])
            thisBag.updateChild(subKey, subValue)
    bagList.append(thisBag)

howManyBagColours = 0
for bagy in bagList:
    #bagy.searchBag()
    if bagy.isChild('shiny gold', bagList):
        howManyBagColours += 1

print(len(bagList))

print(str(howManyBagColours) + ' bags lead to at least one shiny gold bag')