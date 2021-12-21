with open('input.txt') as f:
    lines = f.readlines()

gamma = epsilon = ""

for j in range(12):
    zeroCounter = oneCounter = 0
    for line in lines:
        if line[j] == "1":
            oneCounter += 1
        else:
            zeroCounter += 1

    if oneCounter > zeroCounter:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(f"gamma: {gamma}")
print(f"epsilon: {epsilon}")
print(f"r: {gamma*epsilon}")
