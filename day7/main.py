from itertools import product


def find_operators(values, result):
    operators_possibilities = list(product("*+", repeat=len(values) - 1))
    first = values.pop(0)
    for possibility in operators_possibilities:
        actual_value = first

        for index, item in enumerate(values):
            if possibility[index] == "*":
                actual_value = actual_value * values[index]
            else:
                actual_value += values[index]

            if actual_value > result:
                continue
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
