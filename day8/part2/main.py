with open("input.txt") as f:
    lines = f.readlines()


def get_number_by_len(numbers, lenght, not_needed_chars=None, needed_chars=None):
    for number in numbers:
        if len(number) == lenght:
            if not_needed_chars is None and needed_chars is None:
                return number
            elif not_needed_chars is not None:
                for c in not_needed_chars:
                    if number.find(c) == -1: return number
            else:
                isRight = True
                for c in needed_chars:
                    if number.find(c) == -1:
                        isRight = False
                if isRight: return number
    return None


right_patterns = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def decode_number(keys, values):
    number = ""
    alph = ["A", "B", "C", "D", "E", "F", "G"]
    for value in values:
        for i in range(len(alph)):
            value = value.replace(keys[i], alph[i])
        value = value.lower()
        number += right_patterns["".join(sorted(value))]
    return int(number)


total, signal_pattern, output = 0, [], []

for line in lines:
    line = line.replace("\n", "").split(" | ")
    signal_pattern.append(line[0].split(" "))
    output.append(line[1].split(" "))

for i in range(len(lines)):
    # finds A by the difference of 7 and 1
    seven = get_number_by_len(signal_pattern[i], 3)
    one = get_number_by_len(signal_pattern[i], 2)
    letter_a = seven.replace(one[0], "").replace(one[1], "")

    # finds F by the intersection of 6 and 1
    # and C by removing F from 1
    six = get_number_by_len(signal_pattern[i], 6, not_needed_chars=one)
    letter_f = "".join(set(one).intersection(six))
    letter_c = one.replace(letter_f, "")

    # finds D by the intersection of 3 and 4, removing C and F
    # and B by removing D and F from 4
    three = get_number_by_len(signal_pattern[i], 5, needed_chars=seven)
    four = get_number_by_len(signal_pattern[i], 4)
    letter_d = ("".join(set(three).intersection(four))).replace(letter_c, "").replace(letter_f, "")
    letter_b = four.replace(letter_c, "").replace(letter_d, "").replace(letter_f, "")

    # finds E by the difference of 8 and 9
    nine = get_number_by_len(signal_pattern[i], 6, needed_chars=[letter_c, letter_d])
    eight = get_number_by_len(signal_pattern[i], 7)
    letter_e = "".join(set(nine).symmetric_difference(eight))

    # finds G by the difference of 3 and 4, removing B and A
    letter_g = ("".join(set(three).symmetric_difference(four))).replace(letter_b, "").replace(letter_a, "")

    total += decode_number([letter_a, letter_b, letter_c, letter_d, letter_e, letter_f, letter_g], output[i])

print(total)
