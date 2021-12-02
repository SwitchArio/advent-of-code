with open('input.txt') as f:
    lines = f.readlines()

count = 0
val1 = val2 = 0
n1 = n2 = n3 = 0

for line in lines:
    line = int(line)

    val1 = n1 + n2 + n3

    n3 = n2
    n2 = n1
    n1 = line

    val2 = n1 + n2 + n3

    if val2 > val1:
        count += 1

print(count - 3)
