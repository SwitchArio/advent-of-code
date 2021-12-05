with open('input.txt') as f:
    lines = f.readlines()


def checkVictory(c_board):
    for c_line in c_board:
        flag = True
        for elem in c_line:
            if elem != "x":
                flag = False
        if flag: return True

    for i in range(5):
        flag = True
        for c_line in c_board:
            if c_line[i] != "x":
                flag = False
        if flag: return True
    return False


def boardsChecker(_solutions, _boards):
    for solution in _solutions:
        for a, _board in enumerate(_boards):
            for b, _line in enumerate(_board):
                for c, element in enumerate(_line):
                    if element == solution:
                        boards[a][b][c] = "x"
                        if checkVictory(_board):
                            return _board, solution


solutions = lines[0].replace("\n", "").split(",")
boards, board = [], []

for line in lines[1:]:
    if line == "\n" or line == "-":
        boards.append(board)
        board = []
    else:
        if line.startswith(" "): line = line[1:]
        line = line.replace("  ", " ")
        line = line.replace("\n", "")
        board.append(line.split(" "))

winnerBoard, lastSolution = boardsChecker(solutions, boards)

UnmarkedNumebers = 0

for line in winnerBoard:
    for element in line:
        if element != "x":
            UnmarkedNumebers += int(element)

print(f"solution: {UnmarkedNumebers * int(lastSolution)}")
