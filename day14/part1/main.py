with open("input.txt") as f:
    lines = f.readlines()

pt = lines[0].replace("\n","")  # polymer_template

rules = {}
for line in lines[2:]:
    rule = line.replace("\n", "").split(" -> ")
    rules[rule[0]] = rule[1]


def insert(char, index):
    return pt[:index] + char + pt[index:]

for k in range(10):
    i = 0
    while i < len(pt) - 1:
        pair = pt[i:i + 2]
        if pair in rules.keys():
            pt = insert(rules[pair], i + 1)
            i += 1
        i += 1

print(pt)

counting = {}

for char in pt:
    counting[char] = pt.count(char)
    pt=pt.replace("char","")

print(counting)

print(max(counting.values())-min(counting.values()))
