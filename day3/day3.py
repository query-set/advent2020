from advent_utils.functions import read_file

TREE = "#"


def first():
    cnt = 0
    with open("input.txt", "r") as f:
        lines = f.read()
    mtx = [line for line in lines.split("\n")]
    mtx.pop()
    map_width = len(mtx[0])
    x = y = 0
    while y < len(mtx) - 1:
        y += 1
        x += 3
        if x > map_width - 1:
            x = (x % map_width)
        if mtx[y][x] == TREE:
            cnt += 1

    return cnt


def second(px, py):
    cnt = 0
    with open("input.txt", "r") as f:
        lines = f.read()
    mtx = [line for line in lines.split("\n")]
    mtx.pop()
    map_width = len(mtx[0])
    x = y = 0
    while y < len(mtx) - 1:
        y += py
        x += px
        if x > map_width - 1:
            x = (x % map_width)
        if mtx[y][x] == TREE:
            cnt += 1

    return cnt


def second_multiplier():
    a = second(1, 1)
    b = first()
    c = second(5, 1)
    d = second(7, 1)
    e = second(1, 2)

    print(a, b, c, d, e)
    return a * b * c * d * e


if __name__ == "__main__":
    print("first: ", first())
    print("secon: ", second_multiplier())
