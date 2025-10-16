import time
import string

with open("input.txt") as f:
    lines = f.readlines()

start_time = time.time()

iterations = 40
polymer_input = lines[0].replace("\n", "")  # polymer_template

rules = {}
for line in lines[2:]:
    rule = line.replace("\n", "").split(" -> ")
    rules[rule[0]] = rule[1]  # crea nel dict rules={ ..., rule[0] : rule[1] }

pairList = {}  # lista delle coppie
for i in range(len(polymer_input) - 1):
    pair = polymer_input[i:i + 2]
    if pair not in pairList.keys():
        pairList[pair] = 0
    pairList[pair] += 1

# print(pairList)

for it in range(iterations):
    newPairList = pairList.copy()
    for key in pairList.keys():
        if key in rules.keys():

            pair1 = key[0] + rules[key]
            pair2 = rules[key] + key[1]

            if pair1 not in newPairList.keys():
                newPairList[pair1] = 0
            newPairList[pair1] += pairList[key]

            if pair2 not in newPairList.keys():
                newPairList[pair2] = 0
            newPairList[pair2] += pairList[key]

            newPairList[key] -= pairList[key]

    pairList = newPairList.copy()

# print(pairList)

alphabet = dict.fromkeys(string.ascii_uppercase, 0)
alphabet[polymer_input[0]] += 1
alphabet[polymer_input[-1]] += 1

for key in pairList:
    alphabet[key[0]] = (alphabet[key[0]] + pairList[key])
    alphabet[key[1]] = (alphabet[key[1]] + pairList[key])

finalAlphabet = {}
for key in alphabet.keys():
    if alphabet[key] == 0: continue
    finalAlphabet[key] = alphabet[key] // 2

print(finalAlphabet)

print(max(finalAlphabet.values()) - min(finalAlphabet.values()))
print("--- %s seconds ---" % (round(time.time() - start_time, 5)))
