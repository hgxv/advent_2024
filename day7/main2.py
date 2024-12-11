from itertools import product
import time

start = time.time()


def find_operators(values, result):
    operators_possibilities = list(product("*+|", repeat=len(values) - 1))
    first = values.pop(0)
    values_copy = values.copy()
    for possibility in operators_possibilities:
        actual_value = first

        for index, item in enumerate(values):
            next_value = values_copy[index]
            if possibility[index] == "|":
                if index == 0:
                    actual_value = int(str(first) + str(next_value))
                else:
                    actual_value = int(str(actual_value) + str(item))

            elif possibility[index] == "*":
                actual_value = actual_value * item

            else:
                actual_value += item

        if actual_value == result:
            return result

    return 0


if __name__ == "__main__":
    somme = 0
    with open("input.txt", "r") as file:
        for line in file:
            separator = line.index(":")
            result = int(line[:separator])
            values = [int(x) for x in line[separator + 1 :].split()]
            somme += find_operators(values, result)
        print(somme)

print(time.time() - start)
