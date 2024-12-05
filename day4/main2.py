input = []

with open("input.txt", "r") as file:
    for line in file:
        input.append(line)

xmas_counter = 0

for index_y, line in enumerate(input):
    for index_x, letter in enumerate(line):
        try:
            if letter == "A":
                if index_x < 1 or index_y < 1:
                    continue

                diag1 = [
                    input[index_y - 1][index_x - 1],
                    input[index_y + 1][index_x + 1],
                    letter,
                ]
                diag2 = [
                    input[index_y - 1][index_x + 1],
                    input[index_y + 1][index_x - 1],
                    letter,
                ]
                diag1.sort()
                diag2.sort()
                if diag1 == ["A", "M", "S"] and diag2 == diag1:
                    xmas_counter += 1

        except IndexError:
            pass


print(xmas_counter)
