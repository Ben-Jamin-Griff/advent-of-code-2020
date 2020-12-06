## Part 1
import math

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