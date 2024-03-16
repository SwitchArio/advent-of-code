with open("input.txt") as f:
    lines = f.readlines()
    
    
def cavesWalker(start, allConnections: list[str]):
    allConnCopy = allConnections[:]
    pathsToExplore = []
    counter = 0

    if start == "end": return 1  # path completed! Now i can go back to another one
    if not allConnections: return 0  # if there are no connections it means that's a dead end (a non-valid path)
    for connection in allConnections:
        if start in connection:
            pathsToExplore.append(connection.replace(start, "").replace("-", "").replace("\n", ""))  #writing down the future caves where I will search
            if start == "start" or not start.isupper():  # places where i don't want to go a second time
                allConnCopy.remove(connection)
    for path in pathsToExplore:
        counter += cavesWalker(path, allConnCopy)

    return counter


counter = cavesWalker("start", lines)
print(counter)
