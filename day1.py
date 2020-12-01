## Part 1

# Opening the input
f = open("./data/day1data.txt","r")
lines=f.readlines()
data = []
for x in lines:
    x = x.replace('\n','')
    data.append(int(x))

# Recursion
for x in data:
    tempData = data[:]
    tempData.remove(x)
    for y in tempData:
        if x + y == 2020:
            print('The value of x = ' + str(x) + ' and the value of y = ' + str(y))
            print('The answer to the problem is = ' + str(x*y))

## Part 2
# Double Recursion (there must be a better way)
for x in data:
    tempData = data[:]
    tempData.remove(x)
    for y in tempData:
        tempTempData = tempData[:]
        tempTempData.remove(y)
        for z in tempTempData:
            if x + y + z == 2020:
                print('The value of x = ' + str(x) + ' and the value of y = ' + str(y) + ' and the value of z = ' + str(z))
                print('The answer to the second part of the problem is = ' + str(x*y*z))
                break

## Improvements
f = open("./data/day1data.txt","r")
data = []
for x in f:
    data.append(int(x))