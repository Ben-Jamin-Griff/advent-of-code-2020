## Part 1
import math
from string import ascii_lowercase

# Opening the input
f = open("./data/day6data.txt","r")
lines=f.readlines()
data = []
newValue = ''
for idx, val in enumerate(lines):
    if val != '\n':
        newValue = newValue + val.rstrip()
    else:
        data.append(newValue.rstrip())
        newValue = ''
data.append(newValue.rstrip())

cleanAnswers = []
pointsPerGroup = []
for groupData in data:
    cleanAnswers.append("".join(set(groupData)))
    pointsPerGroup.append(len("".join(set(groupData))))

print('The total points for all groups was ' + str(sum(pointsPerGroup)))

## Part 2

# Opening the input
f = open("./data/day6data.txt","r")
lines=f.readlines()
data = []
group = []
for val in lines:
    if val != '\n':
        group.append(val.rstrip())
    else:
        data.append(group)
        group = []
data.append(group)

totalNewPoints = 0
for groupData in data:
    for letter in ascii_lowercase:
        if sum(letter in answer for answer in groupData) == len(groupData):
            totalNewPoints +=1

print('The new total points for all groups was ' + str(totalNewPoints) + '!')