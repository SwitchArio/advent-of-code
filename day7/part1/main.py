with open("input.txt") as f:
    lines = f.readlines()

initial_positions = lines[0].split(",")

lowestFuel, higherPosition = 0, 0
for position in initial_positions:
    if higherPosition < int(position):
        higherPosition = int(position)
print(higherPosition)

for currentPosition in range(higherPosition+1):
    fuelSpent = 0
    for position in initial_positions:
        fuelSpent += abs(currentPosition - int(position))
    if fuelSpent < lowestFuel or lowestFuel == 0:
        lowestFuel = fuelSpent
print(lowestFuel)
