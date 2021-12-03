with open('input.txt') as f:
    lines = f.readlines()

x = aim = y = 0
for line in lines:
    if line.startswith("forward"):
        x += int(line[7:])
        y += int(line[7:]) * aim
    if line.startswith("up"):
        aim -= int(line[2:])
    if line.startswith("down"):
        aim += int(line[5:])

print(x * y)
