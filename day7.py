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
        #check my bags
        if child in self.children.keys():
            isAChild = True
            return isAChild
        #check my kids bags
        for key in self.children.keys():
            for bag in bagList:
                if bag.name == key:
                    isAChild = bag.isChild(child, bagList)
                    if isAChild:
                        return isAChild
        return

    def countChildren(self, bagList, count):
        for key, val in self.children.items():
            numOfMainBag = int(val)
            for bag in bagList:
                if bag.name == key:
                    subBagCounter = bag.countChildren(bagList, count)
                    count = count + (numOfMainBag+subBagCounter)
        return count

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
            valueForDict = 0
            thisBag.updateChild(bag, valueForDict)
        else:
            bagData = bag.split(" ", 2)
            subKey = bagData[2].replace(' bags', '')
            subKey = subKey.replace(' bag', '')
            subKey = subKey.replace('.', '')
            subValue = int(bagData[1])
            thisBag.updateChild(subKey, subValue)
    bagList.append(thisBag)

howManyBagColours = 0
for bagy in bagList:
    if bagy.isChild('shiny gold', bagList):
        howManyBagColours += 1

print(str(howManyBagColours) + ' bags lead to at least one shiny gold bag')

## Part 2

howManyBags = 1
for bag in bagList:
    if bag.name == 'shiny gold':
        #bag.searchBag()
        howManyBags = bag.countChildren(bagList, howManyBags)

print('Your shiny gold bag contains ' + str(howManyBags) + ' other bags')