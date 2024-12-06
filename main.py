grid = []

with open("input.txt") as file:
    for index, line in enumerate(file):
        grid.append(line)

        if "^" in line:
            x, y = line.index("^"), index

grid_limits = {"x": [0, len(grid[0]) - 1], "y": [0, len(grid) - 1]}


def count_X_occurence():
    x = 1
    for line in grid:
        for item in line:
            if item == "X":
                x += 1

    return x


def guard_patrol(x, y):
    dir_cycle = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir = 0
    corners = []

    while True:
        if (
            x + dir_cycle[dir][0] < grid_limits["x"][0]
            or x + dir_cycle[dir][0] > grid_limits["x"][1]
            or y + dir_cycle[dir][1] < grid_limits["y"][0]
            or y + dir_cycle[dir][1] > grid_limits["y"][1]
        ):
            print(len(corners))
            return count_X_occurence()

        next_x = x + dir_cycle[dir][0]
        next_y = y + dir_cycle[dir][1]

        if grid[next_y][next_x] == "#":
            corners.append([next_y, next_x])
            if dir == 3:
                dir = 0
            else:
                dir += 1

        else:
            replacement = list(grid[y])
            replacement[x] = "X"
            grid[y] = "".join(replacement)
            x += dir_cycle[dir][0]
            y += dir_cycle[dir][1]


print(guard_patrol(x, y))
