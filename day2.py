## Part 1

# Opening the input
f = open("./data/day2data.txt","r")
lines=f.readlines()
data = []
for x in lines:
    data.append(x.rstrip())

correctPasswords = 0
for block in data:
    splitString = block.split()
    splitNums = splitString[0].split('-')
    lowerNum = int(splitNums[0])
    upperNum = int(splitNums[1])
    characterForTesting = splitString[1][0]
    if splitString[2].count(characterForTesting) >= lowerNum and splitString[2].count(characterForTesting) <=upperNum:
        correctPasswords+=1

print('There are ' + str(correctPasswords) + ' correct passwords out of ' + str(len(data)) + ' inputs')

## Part 2
correctPasswords = 0
for block in data:
    isThisPasswordCorrect = 0
    splitString = block.split()
    splitNums = splitString[0].split('-')
    lowerNum = int(splitNums[0])
    upperNum = int(splitNums[1])
    characterForTesting = splitString[1][0]
    if splitString[2][lowerNum-1] == characterForTesting:
        isThisPasswordCorrect+=1
    if splitString[2][upperNum-1] == characterForTesting:
        isThisPasswordCorrect+=1
    if isThisPasswordCorrect == 1:
        correctPasswords+=1

print('There are ' + str(correctPasswords) + ' correct passwords with new policy out of ' + str(len(data)) + ' inputs')