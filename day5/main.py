import math

page_order = {}
updates = []


def is_update_valid(x):
    for index, update in enumerate(x[::-1]):
        for item in x[: len(x) - index]:
            try:
                if item in page_order[update]:
                    return False
            except KeyError:
                continue

    updates.append(x)


with open("input.txt", "r") as file:
    for line in file:
        x = line.strip()

        if "|" in x:
            y = x.split("|")
            page = y[0]
            before = y[1]
            if page not in page_order:
                page_order[page] = [before]

            else:
                page_order[page].append(before)

        elif "," in x:
            is_update_valid(x.split(","))

print(sum([int(update[math.floor(len(update) / 2)]) for update in updates]))
