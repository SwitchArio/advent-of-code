with open("input.txt") as f:
    lines = f.readlines()

table_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
total_score = 0

for line in lines:
    expected = []
    for char in line:

        if char == "\n":
            continue
        elif char == "(":
            expected.insert(0, ")")
        elif char == "[":
            expected.insert(0, "]")
        elif char == "{":
            expected.insert(0, "}")
        elif char == "<":
            expected.insert(0, ">")
        elif char == expected[0]:
            expected.remove(expected[0])
        else:
            total_score += table_points[char]
            break

print(total_score)
