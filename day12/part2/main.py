# I STILL NOT FIGURED OUT HOW TO MAKE IT FASTER 
# this code works but takes 5 minutes to end, by bruteforcing the solution
# not my proudest code lmao

with open("input2.txt") as f:
    lines = f.readlines()

paths = []


def cavesWalker(start, allConnections: list[str], special, fpathc: str, visitedOnceSpecial):
    allConnCopy = allConnections[:]
    pathsToExplore = []
    counter = 0

    # path completed! Now i can go back to another one
    if start == "end":
        if not visitedOnceSpecial: return
        paths.append(fpathc[1:-4])
        return

    # if there are no connections it means that's a dead end (a non-valid path)
    if not allConnections: return

    for connection in allConnections:
        if start in connection:
            
            pathsToExplore.append(connection.replace(start, "").replace("-", "").replace("\n", ""))
            
            if start == "start" or (start.islower() and start != special) or (special == start and visitedOnceSpecial):
                allConnCopy.remove(connection)

    if start == special: visitedOnceSpecial = True
    for path in pathsToExplore:
        fpathc += "," + path
        cavesWalker(path, allConnCopy, special, fpathc, visitedOnceSpecial)
        fpathc = fpathc.rsplit(',', 1)[0]

    return


caves = []

for line in lines:
    seg = line.replace("start", "").replace("end", "").replace("\n", "").split("-")
    for s in seg:
        if s.islower() and s not in caves: caves.append(s)

print(caves)  # all possible special caves

for cave in caves:
    cavesWalker("start", lines, cave, "", False)
    print("once")

count = 0
pp = []
l = len(paths)
for x in paths:
    count += 1
    print((l - count) / l * 100)
    if x not in pp:
        pp.append(x)
print(paths)  # 155477

# for p in paths: print(p)
print(len(pp))
