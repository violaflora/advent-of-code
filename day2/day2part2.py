input = open("input.txt", "r")
lines = input.readlines()

powerSum = 0

def getPower(game):
    redMin = 0
    greenMin = 0
    blueMin = 0
    for part in game:
        part = part[1:]
        part = part.split(" ")
        print(part)
        if "red" in part[1] and int(part[0]) > redMin:
            redMin = int(part[0])
        if "green" in part[1] and int(part[0]) > greenMin:
            greenMin = int(part[0])
        if "blue" in part[1] and int(part[0]) > blueMin:
            blueMin = int(part[0])
    return redMin * greenMin * blueMin

for i in range(len(lines)):
    lines[i] = lines[i].replace(":", ",")
    lines[i] = lines[i].replace(";", ",")
    lines[i] = lines[i].split(",")
    lines[i].pop(0)
    powerSum += getPower(lines[i])
    print(powerSum)