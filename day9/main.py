import re

test = "233313312141413140222"


def create_id(data):
    id = []
    index_id = 0
    for index, item in enumerate(data):
        if index % 2 == 0:
            for i in range(int(item)):
                id.append(str(index_id))
            index_id += 1

        else:
            for i in range(int(item)):
                id.append(".")

    return reorder(id)


def reorder(id):
    for index, item in enumerate(id):
        if item == ".":
            if not re.search("\d", "".join(id[index:])):
                break
            replacement = ""
            for i, j in enumerate(id[::-1]):
                if j.isnumeric():
                    replacement = j
                    id[-i - 1] = "."
                    break
            id[index] = replacement

    return id


def checksum(id):
    result = 0

    for index, item in enumerate(id):
        if not re.search("\d", "".join(id[index:])):
            break
        result += int(item) * index

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.readline()
    id = create_id(test)
    print(checksum(id))
