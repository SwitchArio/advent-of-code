with open("input.txt") as f:
    lines = f.readlines()

counter, signal_pattern, output = 0, [], []

for line in lines:
    line = line.replace("\n", "").split(" | ")
    signal_pattern.append(line[0].split(" "))
    output.append(line[1].split(" "))

for numbers in output:
    for number in numbers:
        if len(number) == 2 or len(number) == 4 or len(number) == 3 or len(number) == 7:
            counter += 1

print(counter)
