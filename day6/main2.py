import time

grid = []
visited = []

start = time.time()

with open("input.txt") as file:
    for index, line in enumerate(file):
        grid.append(line)

        if "^" in line:
            x, y = line.index("^"), index

grid_limits = {"x": [0, len(grid[0]) - 1], "y": [0, len(grid) - 1]}


def count_X_occurence(grid):
    x = 1
    for line in grid:
        for item in line:
            if item == "X":
                x += 1

    return x


def guard_patrol(x, y, grid, has_visited_yet=False):
    dir_cycle = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir = 0
    is_loophole = 0
    corners = {}

    while True:
        if (
            x + dir_cycle[dir][0] < grid_limits["x"][0]
            or x + dir_cycle[dir][0] > grid_limits["x"][1]
            or y + dir_cycle[dir][1] < grid_limits["y"][0]
            or y + dir_cycle[dir][1] > grid_limits["y"][1]
        ):
            if not has_visited_yet:
                visited.append([x, y])
            return is_loophole

        next_x = x + dir_cycle[dir][0]
        next_y = y + dir_cycle[dir][1]

        if grid[next_y][next_x] == "#":
            if (next_x, next_y) not in corners:
                corners[(next_x, next_y)] = [(x, y)]
            else:
                if (x, y) in corners[(next_x, next_y)]:
                    return 1
                corners[(next_x, next_y)].append((x, y))

            if dir == 3:
                dir = 0
            else:
                dir += 1

        else:
            if not has_visited_yet:
                if [x, y] not in visited:
                    visited.append([x, y])

            replacement = list(grid[y])
            replacement[x] = "X"
            grid[y] = "".join(replacement)
            x += dir_cycle[dir][0]
            y += dir_cycle[dir][1]


def try_to_block(x, y):
    loopholes = 0
    for coordonates in visited[1:]:
        index_y = coordonates[1]
        index_x = coordonates[0]
        new_grid = grid.copy()
        x_copy = x
        y_copy = y
        replacement = list(new_grid[index_y])
        replacement[index_x] = "#"
        new_grid[index_y] = "".join(replacement)
        loopholes += guard_patrol(x_copy, y_copy, new_grid, True)
    print(loopholes)


guard_patrol(x, y, grid)
try_to_block(x, y)
stop = time.time()
print(stop - start)
