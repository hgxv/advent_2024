def check_valid(line):
    last_item = False
    last_space = False

    for item in line.split():

        if not last_item:
            last_item = item
            continue

        space = int(last_item) - int(item)
        print(f"{last_item} - {item} = {space}")

        if not last_space:
            if space < 0:
                last_space = "neg"
            else:
                last_space = "pos"

        if abs(space) < 1 or abs(space) > 3:
            return False

        if space < 0 and last_space == "pos":
            return False

        elif space > 0 and last_space == "neg":
            print("b")
            return False

        last_item = item

    return True


safe_levels = 0

with open("input.txt", "r") as file:
    for line in file:
        if check_valid(line):
            safe_levels += 1

print(safe_levels)
