from itertools import combinations

grid = []
antennas = {}
antinode_positions = set()

with open("input.txt", "r") as file:
    for index_y, line in enumerate(file):
        grid.append(line.strip())
        for index_x, item in enumerate(line.strip()):
            if item.isalnum():
                antennas.setdefault(item, []).append((index_y, index_x))

grid_limits = [len(grid) - 1, len(grid[0]) - 1]


def is_within_limits(x, y):
    return 0 <= x <= grid_limits[0] and 0 <= y <= grid_limits[1]


def calculate_antinodes(pair):
    antenna_1 = pair[0]
    antenna_2 = pair[1]
    space = (antenna_1[0] - antenna_2[0], antenna_1[1] - antenna_2[1])
    antinode_1 = (antenna_1[0] + space[0], antenna_1[1] + space[1])
    antinode_2 = (antenna_2[0] - space[0], antenna_2[1] - space[1])

    if is_within_limits(*antinode_1):
        antinode_positions.add(antinode_1)

    if is_within_limits(*antinode_2):
        antinode_positions.add(antinode_2)


if __name__ == "__main__":
    for antenna in antennas:
        pairs = combinations(antennas[antenna], 2)
        for pair in pairs:
            calculate_antinodes(pair)
    print(len(antinode_positions))
