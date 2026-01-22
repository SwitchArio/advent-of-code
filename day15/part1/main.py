import time


def getNeighbors(pos: tuple):
    toReturn = set()
    if pos[0] < MaxRows - 1: toReturn.add((pos[0] + 1, pos[1]))
    if pos[0] > 0: toReturn.add((pos[0] - 1, pos[1]))
    if pos[1] < MaxColumns - 1: toReturn.add((pos[0], pos[1] + 1))
    if pos[1] > 0: toReturn.add((pos[0], pos[1] - 1))
    return toReturn


with open("input.txt") as f:
    lines = f.readlines()

start_time = time.time()

Grid = []
for line in lines:
    currLine = [int(c) for c in line.replace("\n", "")]
    Grid.append(currLine)

MaxRows = len(Grid)
MaxColumns = len(Grid[0])
DistancesGrid = [[-1 for _ in range(MaxColumns)] for _ in range(MaxRows)]
DistancesGrid[0][0] = 0

StartPos = (0, 0)
FinalPos = (MaxRows - 1, MaxColumns - 1)

# Using tuple + set + min for Dijstra
unvisited_list = {(i, j) for i in range(MaxRows) for j in range(MaxColumns)}
unvisited_list.remove((0, 0))

visited_list = set()
valuing_list = {StartPos}

while valuing_list and FinalPos not in visited_list:

    # Here it's a o(n^2) but for a 100x100 it's cool
    justVisited = min(valuing_list, key=lambda p: DistancesGrid[p[0]][p[1]])
    visited_list.add(justVisited)
    valuing_list.remove(justVisited)

    for neighbor in getNeighbors(justVisited):
        if neighbor in visited_list: continue

        x, y = neighbor
        xNode, yNode = justVisited
        newDist = Grid[x][y] + DistancesGrid[xNode][yNode]

        if DistancesGrid[x][y] == -1 or DistancesGrid[x][y] > newDist:
            DistancesGrid[x][y] = newDist
            valuing_list.add(neighbor)


xF, yF = FinalPos
print(DistancesGrid[xF][yF])

print("--- %s seconds ---" % (round(time.time() - start_time, 5)))
