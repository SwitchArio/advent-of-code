with open("input.txt") as f:
    lines = f.readlines()

heightmap, largest_sizes = [], [0, 0, 0]


def basin_explorer(raw, column, heightmap):
    height = int(heightmap[raw][column])
    if height == 9:
        return 0, heightmap
    basin_size = 1
    heightmap[raw][column] = "x"

    if column > 0:
        left = heightmap[raw][column - 1]

        if left != "x" and int(left) > height:
            temp, heightmap = basin_explorer(raw, column - 1, heightmap)
            basin_size += temp

    if column != 99:
        right = heightmap[raw][column + 1]

        if right != "x" and int(right) > height:
            temp, heightmap = basin_explorer(raw, column + 1, heightmap)
            basin_size += temp

    if raw > 0:
        down = heightmap[raw - 1][column]

        if down != "x" and int(down) > height:
            temp, heightmap = basin_explorer(raw - 1, column, heightmap)
            basin_size += temp

    if raw != 99:
        up = heightmap[raw + 1][column]

        if up != "x" and int(up) > height:
            temp, heightmap = basin_explorer(raw + 1, column, heightmap)
            basin_size += temp

    return basin_size, heightmap


for line in lines:
    line = line.replace("\n", "")
    heightmap.append(list(line))

heightmap_copy = [x[:] for x in heightmap]

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
            basin_size, heightmap_copy = basin_explorer(raw, column, heightmap_copy)
            largest_sizes.sort()
            if basin_size > largest_sizes[0]:
                largest_sizes[0] = basin_size

print(f"result: {largest_sizes[0] * largest_sizes[1] * largest_sizes[2]}")
