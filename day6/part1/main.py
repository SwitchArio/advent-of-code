with open("input.txt") as f:
    lines = f.readlines()

initial_counters = lines[0].split(",")
DAYS = 80

all_fish = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

order = [0, 8, 7, 6, 5, 4, 3, 2, 1, 0, 8]

for counter in initial_counters:
    counter = int(counter)
    all_fish[counter] += 1

for day in range(DAYS):
    temp, temp2 = 0, 0
    for i, val in enumerate(order):
        if i == 10: continue
        if i == 0: all_fish[7] += all_fish[0]
        temp2 = all_fish[order[i+1]]
        all_fish[order[i+1]] = temp
        temp = temp2

total = 0
for i in range(9): total += all_fish[i]
print(total)
