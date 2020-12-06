## Part 1
import math

# Opening the input
f = open("./data/day5data.txt","r")
lines=f.readlines()
data = []
for x in lines:
    data.append(x.rstrip())

rowValues = []
seatValues = []
for seatReference in data:
    rowIdx = [0, 127]
    seatIdx = [0, 7]
    for val in seatReference:
        if val == 'F':
            rowIdx[1] = rowIdx[1] - math.ceil((rowIdx[1]-rowIdx[0])/2)
        elif val == 'B':
            rowIdx[0] = rowIdx[0] + math.ceil((rowIdx[1]-rowIdx[0])/2)
        elif val == 'L':
            seatIdx[1] = seatIdx[1] - math.ceil((seatIdx[1]-seatIdx[0])/2)
        elif val == 'R':
            seatIdx[0] = seatIdx[0] + math.ceil((seatIdx[1]-seatIdx[0])/2)

    rowValues.append(rowIdx[0])
    seatValues.append(seatIdx[0])

seatID = [x*8 + y for x, y in zip(rowValues, seatValues)]

print('The highest seat ID value is ' + str(max(seatID)) + '!')

## Part 2

for potentialSeat in range(0,880):
    if potentialSeat not in seatID:
        if potentialSeat+1 in seatID and potentialSeat-1 in seatID:
            print('Our seat is ' + str(potentialSeat))

        