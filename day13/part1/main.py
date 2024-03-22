import numpy as np

with open("input.txt") as f:
    lines = f.readlines()


def printm(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


coordinates = []
instructions = []
xmax = ymax = 0

for line in lines:
    if "," in line:
        xy = line.replace("\n", "").split(",")
        x = int(xy[0])
        y = int(xy[1])
        xmax = x if x > xmax else xmax
        ymax = y if y > ymax else ymax
        coordinates.append([x, y])
    elif "fold" in line:
        tmp = line.replace("fold along ", "").replace("\n", "").split("=")
        instructions.append([tmp[0], int(tmp[1])])

# fold along x=655
for c in coordinates:
    if c[0] > 655:
        c[0] = 655 * 2 - c[0]  # 655-(c[0]-655)

xmax = (xmax/2)-1

board = [[0 for x in range(xmax + 1)] for y in range(ymax + 1)]
for x, y in coordinates:
    board[y][x] = 1

b=np.matrix(board)
print(b.sum())
