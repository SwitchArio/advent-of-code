with open('input.txt') as f:
    lines = f.readlines()


def filter1(index, numbers):
    newNumbers = []

    zeroCounter = oneCounter = 0
    for n in numbers:
        if n[index] == "1":
            oneCounter += 1
        else:
            zeroCounter += 1

    if oneCounter >= zeroCounter:
        mostCommon = "1"
    else:
        mostCommon = "0"

    for n in numbers:
        if n[index] == mostCommon:
            newNumbers.append(n)

    if len(newNumbers) != 1:
        return filter1(index + 1, newNumbers)
    else:
        return newNumbers


def filter2(index, numbers):
    newNumbers = []

    zeroCounter = oneCounter = 0
    for n in numbers:
        if n[index] == "1":
            oneCounter += 1
        else:
            zeroCounter += 1

    if oneCounter >= zeroCounter:
        lessCommon = "0"
    else:
        lessCommon = "1"

    for n in numbers:
        if n[index] == lessCommon:
            newNumbers.append(n)

    if len(newNumbers) != 1:
        return filter2(index + 1, newNumbers)
    else:
        return newNumbers


CO2Rating = int(filter2(0, lines)[0], 2)
oGeneratorRating = int(filter1(0, lines)[0], 2)
print(oGeneratorRating)
print(CO2Rating)

print(f"CO2Rating: {CO2Rating}")
print(f"oGeneratorRating: {oGeneratorRating}")
print(f"r: {oGeneratorRating * CO2Rating}")
