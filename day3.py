## Part 1
import math
from functools import reduce

# Opening the input
f = open("./data/day3data.txt","r")
lines=f.readlines()
data = []
for x in lines:
    data.append(x.rstrip())

# Increasing the size of the list to perform analysis
lengthRow = len(data[0])
lengthdata = len(data)
multiplier = math.ceil(lengthdata/lengthRow)

squareData = []
for line in data:
    newLine = line
    for i in range(1,multiplier*7):
        newLine = newLine + line
    squareData.append(newLine)

# Checking locations
indexChecker = 0
values = []
for row in squareData:
    values.append(row[indexChecker])
    indexChecker +=3

trees = values.count('#')

print('Following the initial trajectory you would encouter ' + str(trees) + ' trees!')
    
# Checking locations
indexCheckerChangeValues = [1,3,5,7]
slopeAnswers = []
for changeChecker in indexCheckerChangeValues:
    indexChecker = 0
    values = []
    for row in squareData:
        values.append(row[indexChecker])
        indexChecker +=changeChecker
    trees = values.count('#')
    slopeAnswers.append(trees)

indexChecker = 0
values = []
for i, row in enumerate(squareData):
    if (i % 2) == 0:  
        values.append(row[indexChecker])
        indexChecker +=1
trees = values.count('#')
slopeAnswers.append(trees)

print(slopeAnswers)

finalCalc = reduce(lambda x, y: x*y, slopeAnswers)

print('The multiplication of all the tress encountered for the different slope is ' + str(finalCalc))



