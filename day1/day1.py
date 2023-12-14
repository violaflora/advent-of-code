sum = 0

input = open("input.txt", "r")
for line in input:
    digitString = ""
    for char in line:
        if char.isdigit():
            digitString += char
    lineValue = int(digitString[0] + digitString[-1])
    sum += lineValue
print(sum)