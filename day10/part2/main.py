with open("input.txt") as f:
    lines = f.readlines()

table_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
total_score, incomplete_lines = [], []

for line in lines:
    expected = []
    for char in line:

        if char == "\n":
            incomplete_lines.append(line)
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
            break

for line in incomplete_lines:
    expected, score = [], 0
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
            raise Exception(f"expected: {expected}\nchar: {char}\nline: {line}")
    for char in expected:
        score *= 5
        score += table_points[char]
    total_score.append(score)

total_score.sort()
index = int((len(total_score)-1)/2)
print(total_score[index])
