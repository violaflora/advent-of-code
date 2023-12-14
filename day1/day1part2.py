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
            print(scanningString)
            if "one" in scanningString:
                digitString += "1"
                scanningString = scanningString[-1]
            elif "two" in scanningString:
                digitString += "2"
                scanningString = scanningString[-1]
            elif "three" in scanningString:
                digitString += "3"
                scanningString = scanningString[-1]
            elif "four" in scanningString:
                digitString += "4"
                scanningString = scanningString[-1]
            elif "five" in scanningString:
                digitString += "5"
                scanningString = scanningString[-1]
            elif "six" in scanningString:
                digitString += "6"
                scanningString = scanningString[-1]
            elif "seven" in scanningString:
                digitString += "7"
                scanningString = scanningString[-1]
            elif "eight" in scanningString:
                digitString += "8"
                scanningString = scanningString[-1]
            elif "nine" in scanningString:
                digitString += "9"
                scanningString = scanningString[-1]
            
    lineValue = int(digitString[0] + digitString[-1])
    print(lineValue)
    sum += lineValue
print(sum)
