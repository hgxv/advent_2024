import re
import time

test = "233313312141413140222"


def create_id(data):
    id = []
    free_spaces = []
    index_id = 0
    for index, item in enumerate(data):
        if index % 2 == 0:
            for i in range(int(item)):
                id.append(str(index_id))
            index_id += 1

        else:
            free_spaces.append([x for x in range(len(id), len(id) + int(item))])
            for i in range(int(item)):
                id.append(".")

    return reorder(id, free_spaces)


def reorder(id, free_spaces):
    used = []
    for index in range(-1, -len(id), -1):
        item = id[index]
        if not item.isnumeric() or item in used:
            pass

        if not re.search("\.", "".join(id[:index])):
            break

        item_count = id.count(item)

        for spaces in free_spaces:
            if len(spaces) < item_count:
                continue
            if spaces[0] > len(id) - abs(index) - 1:
                break

            used.append(int(item))
            for x in range(item_count):
                i = spaces.pop(0)
                id[i] = item
                id[index - x] = "."
            break

    return id


def count_free_space(id):
    index = 0
    while id[index] == ".":
        index += 1
    return index


def checksum(id):
    result = 0

    for index, item in enumerate(id):
        if item.isnumeric():
            result += int(item) * index

    return result


if __name__ == "__main__":
    start = time.time()
    with open("input.txt", "r") as f:
        input = f.readline()
    id = create_id(input)
    print(checksum(id))
    print(time.time() - start)
