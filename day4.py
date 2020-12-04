## Part 1

# Opening the input
f = open("./data/day4data.txt","r")
lines=f.readlines()
data = []
newValue = ''
for idx, val in enumerate(lines):
    if val != '\n':
        newValue = newValue + ' ' + val.rstrip()
    else:
        data.append(newValue.rstrip())
        newValue = ''
data.append(newValue.rstrip())

passports = []
for val in data:
    passport = {}
    passportData = val.split()
    for entry in passportData:
        entrySplit = entry.split(':')
        passport[entrySplit[0]] = entrySplit[1]
    passports.append(passport)

correctPassports = 0
values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
    if all (k in passport for k in values):
        correctPassports += 1

print('There are ' + str(correctPassports) + ' valid passports! Out of ' + str(len(passports)) + (' total passports.'))

# Part 2
correctPassports = 0
values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
    if all (k in passport for k in values):
        checker = 0
        for key in passport:
            if key == 'byr':
                if passport[key].isdigit() and int(passport[key]) >= 1920 and int(passport[key]) <= 2002:
                    checker +=1
            if key == 'iyr':
                if passport[key].isdigit() and int(passport[key]) >= 2010 and int(passport[key]) <= 2020:
                    checker +=1
            if key == 'eyr':
                if passport[key].isdigit() and int(passport[key]) >= 2020 and int(passport[key]) <= 2030:
                    checker +=1
            if key == 'hgt':
                if "cm" in passport[key]:
                    num = int("".join(filter(str.isdigit, passport[key])))
                    if num >= 150 and num <= 193:
                        checker +=1
                elif "in" in passport[key]:
                    num = int("".join(filter(str.isdigit, passport[key])))
                    if num >= 59 and num <= 76:
                        checker +=1
            if key == 'hcl':
                if passport[key][0] == '#':
                    if len(passport[key][1:]) == 6:
                        strChecker = 0
                        for c in passport[key][1:]:
                            if c.isdigit() and int(c) >=0 and int(c) <=9:
                                strChecker += 1
                            elif c in 'abcdef':
                                strChecker += 1
                        if strChecker == 6:
                            checker +=1
            if key == 'ecl':
                if any(passport[key] in s for s in ['amb' 'blu' 'brn' 'gry' 'grn' 'hzl' 'oth']):
                    checker += 1
            if key == 'pid':
                if passport[key].isdigit() and len(passport[key]) == 9:
                    checker +=1
        if checker == 7:
            correctPassports += 1

print('There are ' + str(correctPassports) + ' valid passports after introducing validation')