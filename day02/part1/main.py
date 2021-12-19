with open('input.txt') as f:
    lines = f.readlines()
    
x = y = 0
for line in lines:
    if line.startswith("forward"):
        x += int(line[7:])
    if line.startswith("up"):
        y -= int(line[2:])
    if line.startswith("down"):
        y += int(line[5:])

print(x * y)
