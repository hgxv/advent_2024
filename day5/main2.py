import math

page_order = {}
updates = []
result = 0


def is_update_not_valid(x):
    for index, update in enumerate(x[::-1]):
        for item in x[: len(x) - index]:
            try:
                if item in page_order[update]:
                    updates.append(x)
                    return False
            except KeyError:
                continue


def rectify_update(update):
    index = 1
    while True:
        if index == len(update):
            return int(update[math.floor(len(update) / 2)])

        last_element = update[-index]
        for element in update[:-index]:
            try:
                if element in page_order[last_element]:
                    update.pop(-index)
                    update.insert(0, last_element)
                    break

            except KeyError:
                continue

        else:
            index += 1


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
            is_update_not_valid(x.split(","))


for update in updates:
    result += rectify_update(update)

print(result)
