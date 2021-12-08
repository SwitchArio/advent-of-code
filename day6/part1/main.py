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

for counter in initial_counters:
    counter = int(counter)
    all_fish[counter] += 1

for day in range(DAYS):
    next_value, saved_value = 0, 0
    for i in range(9, -1, -1):
        if i == 0:
            all_fish[6] += next_value
            all_fish[8] += next_value
        else:
            saved_value = all_fish[i - 1]  # save the value of the next one
            all_fish[i - 1] = next_value  # put the value in the next one
            next_value = saved_value  # the saved value is become the next value
total = 0
for i in range(9):
    total += all_fish[i]
print(total)
