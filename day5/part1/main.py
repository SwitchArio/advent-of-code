with open("input.txt") as f:
    lines = f.readlines()


class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"{self.x} ; {self.y}"

    def getPointsBetween(self, point):
        if self.x == point.x:
            if point.y > self.y:
                bigger = point.y
                lower = self.y
            else:
                bigger = self.y
                lower = point.y

            return [[self.x, y] for y in range(bigger, lower - 1, -1)]
        else:
            if point.x > self.x:
                bigger = point.x
                lower = self.x
            else:
                bigger = self.x
                lower = point.x

            return [[x, self.y] for x in range(bigger, lower - 1, -1)]


a_points, b_points = [], []

for line in lines:
    line = line.replace("\n", "").split(" -> ")

    a = line[0].split(",")
    b = line[1].split(",")

    if a[0] == b[0] or a[1] == b[1]:
        a_points.append(Point(a[0], a[1]))
        b_points.append(Point(b[0], b[1]))

# finding the higher x and y value for the board width and heigh
hX, hY = 0, 0

for a in a_points:
    if a.x > hX: hX = a.x
    if a.y > hY: hY = a.y
for b in b_points:
    if b.x > hX: hX = b.x
    if b.y > hY: hY = b.y

# setup of the board: {hX} number of elements for each of {hY} lists
board = [[0 for x in range(hX + 1)] for y in range(hY + 1)]

# filling the cells with the lines
for j, a in enumerate(a_points):
    pointsToMark = a.getPointsBetween(b_points[j])
    for pToMark in pointsToMark:
        board[pToMark[1]][pToMark[0]] += 1

# counting the intersections
intersectionsCounter = 0
for raw in board:
    for cell in raw:
        if cell >= 2:
            intersectionsCounter += 1

print(f"{intersectionsCounter}")
