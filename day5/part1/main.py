with open("input.txt") as f:
    lines = f.readlines()


class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"{self.x} ; {self.y}"


a_points, b_points = [], []

for line in lines:
    line = line.replace("\n", "").split(" -> ")

    a = line[0].split(",")
    b = line[1].split(",")

    if a[0] == b[0] or a[1] == b[1]:
        a_points.append(Point(a[0], a[1]))
        b_points.append(Point(b[0], b[1]))


board = [[]]
hX, hY = 0, 0

for a in a_points:
    if a.x > hX: hX = a.x
    if a.y > hY: hY = a.y
for b in b_points:
    if b.x > hX: hX = b.x
    if b.y > hY: hY = b.y

for c in range(hX):
    for r in range(hY):
        board[r][c] = 0

print(f"{hX} {hY}")
# https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array




# for i in range(len(a_points)):
#     print(f"{a_points[i]} - {b_points[i]}")
