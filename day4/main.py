input = []

with open("input.txt", "r") as file:
    for line in file:
        input.append(line)

xmas_counter = 0
word = "XMAS"

directions = [
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, -1),
    (0, +1),
    (+1, -1),
    (+1, 0),
    (+1, +1),
]


def search_letter(x, y, direction, letter_index):
    try:
        if x < 0 or y < 0:
            return 0
        result = 0

        if input[x][y] == word[letter_index]:
            print(f"{x} {y} - {word[letter_index]}")
            if word[letter_index] == "S":

                return 1
            letter_index += 1
            result = search_letter(
                x + int(direction[0]), y + int(direction[1]), direction, letter_index
            )

        return result

    except IndexError:
        return 0


for index_y, line in enumerate(input):
    for index_x, letter in enumerate(line):
        if letter == "X":
            letter_index = 1

            for direction in directions:
                xmas_counter += search_letter(
                    index_y + direction[0],
                    index_x + direction[1],
                    direction,
                    letter_index,
                )

print(xmas_counter)
