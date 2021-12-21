with open("input.txt") as f:
    lines = f.readlines()


def distanceCost(pos1, pos2):
    distance = abs(pos1-pos2)
    stepCost, totalCOst = 1, 0

    for i in range(distance):
        totalCOst += stepCost
        stepCost += 1

    return totalCOst


initial_positions = lines[0].split(",")

lowestFuel, higherPosition = 0, 0
for position in initial_positions:
    if higherPosition < int(position):
        higherPosition = int(position)

for currentPosition in range(higherPosition + 1):
    fuelSpent = 0
    for position in initial_positions:
        fuelSpent += distanceCost(currentPosition, int(position))
    if fuelSpent < lowestFuel or lowestFuel == 0:
        lowestFuel = fuelSpent
    else: break
print(lowestFuel)
