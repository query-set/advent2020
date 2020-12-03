from advent_utils.functions import read_file


def first():
    counter = 0
    for line in read_file():
        amount, char, code = line.split()
        min_s, max_s = amount.split("-")
        char = char[0]
        occ = code.count(char)
        if occ >= int(min_s) and occ <= int(max_s):
            counter += 1
    return counter


def second():
    counter = 0
    for line in read_file():
        amount, char, code = line.split()
        posa, posb = amount.split("-")
        char = char[0]
        posa, posb = int(posa) - 1, int(posb) - 1
        if (
                (code[posa] == char and code[posb] != char)
                or (code[posb] == char and code[posa] != char)
        ):
            counter += 1

    return counter


if __name__ == "__main__":
    print("first: ", first())
    print("second: ", second())
