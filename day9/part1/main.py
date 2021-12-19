with open("input.txt") as f:
    lines = f.readlines()

heightmap, risk_level_sum = [], 0

for line in lines:
    line = line.replace("\n", "")
    heightmap.append(list(line))

for raw in range(100):
    for column in range(100):
        isLow = True
        height = int(heightmap[raw][column])

        if column > 0:
            if height > int(heightmap[raw][column - 1]):
                isLow = False

        if column != 99:
            if height > int(heightmap[raw][column + 1]):
                isLow = False

        if raw > 0:
            if height > int(heightmap[raw - 1][column]):
                isLow = False

        if raw != 99:
            if height > int(heightmap[raw + 1][column]):
                isLow = False

        if isLow:
            risk_level_sum += (height + 1)

print(risk_level_sum)
