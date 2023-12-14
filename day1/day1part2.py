numsDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

sum = 0

input = open("input.txt", "r")
for line in input:
    digitString = ""
    scanningString = ""
    for char in line:
        if char.isdigit():
            digitString += char
            scanningString = ""
        # need to account for cases like "ninedvbzngtv7rtb4ksrmveightwofjn", will return eight as final digit instead of two
        # "eightwoeightwo"
        else:
            scanningString += char
            for key in numsDict:
                if key in scanningString:
                    digitString += numsDict[key]
                    scanningString = scanningString[-1]
            
    lineValue = int(digitString[0] + digitString[-1])
    sum += lineValue
print(sum)