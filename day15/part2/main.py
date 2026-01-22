import time
import heapq


def getNeighbors(pos: tuple):
    if pos[0] < MaxRows - 1: yield (pos[0] + 1, pos[1])
    if pos[0] > 0: yield (pos[0] - 1, pos[1])
    if pos[1] < MaxColumns - 1: yield (pos[0], pos[1] + 1)
    if pos[1] > 0: yield (pos[0], pos[1] - 1)


with open("input.txt") as f:
    lines = f.readlines()

start_time = time.time()
TIMES_LARGER = 5

Grid = []
for line in lines:
    currLine = [int(c) for c in line.replace("\n", "")]
    MaxColumns = len(currLine)
    for i in range(1, TIMES_LARGER):
        copy = [((x - 1 + i) % 9) + 1 for x in currLine[:MaxColumns]]
        currLine.extend(copy)
    Grid.append(currLine)

MaxRows = len(Grid)

for i in range(1, TIMES_LARGER):
    for line in Grid[:MaxRows]:
        copy = [((x - 1 + i) % 9) + 1 for x in line]
        Grid.append(copy)


MaxRows = len(Grid)
MaxColumns = len(Grid[0])
StartPos = (0, 0)
FinalPos = (MaxRows - 1, MaxColumns - 1)

DistancesGrid = [[-1 for _ in range(MaxColumns)] for _ in range(MaxRows)]
DistancesGrid[0][0] = 0

visited_list = set()
valuing_list = []
heapq.heappush(valuing_list, (0, StartPos))

while valuing_list and FinalPos not in visited_list:

    # Here it's a o(log(k))
    oldDist, justVisited = heapq.heappop(valuing_list)

    xNode, yNode = justVisited
    if oldDist != DistancesGrid[xNode][yNode]: continue

    visited_list.add(justVisited)

    for neighbor in getNeighbors(justVisited):
        if neighbor in visited_list: continue

        x, y = neighbor
        newDist = Grid[x][y] + DistancesGrid[xNode][yNode]

        if DistancesGrid[x][y] == -1 or DistancesGrid[x][y] > newDist:
            DistancesGrid[x][y] = newDist
            heapq.heappush(valuing_list, (newDist, neighbor))

xF, yF = FinalPos
print(DistancesGrid[xF][yF])

print("--- %s seconds ---" % (round(time.time() - start_time, 5)))
