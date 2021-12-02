with open('input.txt') as f:
    lines = f.readlines()

count = 0
previous_line = 0

for line in lines:
    if int(line) > previous_line:
        count += 1
    previous_line = int(line)

print(count - 1)
