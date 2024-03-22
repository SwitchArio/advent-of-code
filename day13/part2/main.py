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


for fold in instructions:
    if "x" in fold:
        for c in coordinates:
            if c[0] > fold[1]:
                c[0] = fold[1] * 2 - c[0]
        xmax = int(xmax / 2) - 1
    if "y" in fold:
        for c in coordinates:
            if c[1] > fold[1]:
                c[1] = fold[1] * 2 - c[1]
        ymax = int(ymax / 2) - 1

board = [["." for x in range(xmax + 1)] for y in range(ymax + 1)]
for x, y in coordinates:
    board[y][x] = "#"

printm(board)
