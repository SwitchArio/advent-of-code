with open("input.txt") as f:
    lines = f.readlines()


class DumboOctopuses:
    totalFlashes = 0

    def __init__(self, energy_level):
        self.energy_level = energy_level

    def step_flash(self):
        self.energy_level += 1
        if self.energy_level == 10:
            DumboOctopuses.totalFlashes += 1
            return 10
        return self.energy_level

    def update(self):
        if self.energy_level >= 10:
            self.energy_level = 0

    def __str__(self):
        return f"e_level: {self.energy_level}"


def flash(raw, column):
    if column > 0:
        if board[raw][column - 1].step_flash() == 10:
            flash(raw, column - 1)
        if raw != 9:
            if board[raw + 1][column - 1].step_flash() == 10:
                flash(raw + 1, column - 1)
        if raw > 0:
            if board[raw - 1][column - 1].step_flash() == 10:
                flash(raw - 1, column - 1)

    if column != 9:
        if board[raw][column + 1].step_flash() == 10:
            flash(raw, column + 1)
        if raw != 9:
            if board[raw + 1][column + 1].step_flash() == 10:
                flash(raw + 1, column + 1)
        if raw > 0:
            if board[raw - 1][column + 1].step_flash() == 10:
                flash(raw - 1, column + 1)

    if raw > 0:
        if board[raw - 1][column].step_flash() == 10:
            flash(raw - 1, column)

    if raw != 9:
        if board[raw + 1][column].step_flash() == 10:
            flash(raw + 1, column)


board, steps, flashes = [], -1, 0

for line in lines:
    board.append([DumboOctopuses(x) for x in list(map(int, line.replace("\n", "")))])

while True:
    steps += 1
    flashes = 0
    
    for raw in board:
        for element in raw:
            if element.energy_level >= 10:
                flashes += 1
            element.update()

    for raw in range(10):
        for column in range(10):
            if board[raw][column].step_flash() == 10:
                flash(raw, column)

    if flashes == 100:
        print(steps)
        break
