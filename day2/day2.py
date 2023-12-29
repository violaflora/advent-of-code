input = open("day2/input.txt", "r")
lines = input.readlines()
idSum = 0

def isGameValid(game):
    for part in game:
        part = part[1:]
        part = part.split(" ")
        print(part)
        if "red" in part[1] and int(part[0]) > 12:
            return False
        if "green" in part[1] and int(part[0]) > 13:
            return False
        if "blue" in part[1] and int(part[0]) > 14:
            return False
    return True

for i in range(len(lines)):
    lines[i] = lines[i].replace(":", ",")
    lines[i] = lines[i].replace(";", ",")
    lines[i] = lines[i].split(",")
    lines[i].pop(0)
    if isGameValid(lines[i]):
        idSum += i+1
    print(idSum)