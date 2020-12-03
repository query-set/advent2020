FILENAME = "input.txt"


def find_matching_entries():
    with open(FILENAME, "r") as f:
        data1 = [int(line) for line in f.readlines()]

    data2 = data1[1:]
    data3 = data2[1:]
    for x in data1:
        for y in data2:
            for z in data3:
                if (x + y + z) == 2020:
                    return x * y * z


if __name__ == "__main__":
    print(find_matching_entries())
