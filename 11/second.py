#!/usr/bin/env python3

# Axial Coordinates are used here.
# See: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
MOVEMENTS = {
    "n": (0, -1),
    "s": (0, +1),

    "ne": (+1, -1),

    "nw": (-1, 0),

    "se": (+1, 0),

    "sw": (-1, +1),
}


def path_length(x, y):
    return (abs(x) + abs(x + y) + abs(y)) / 2


def main():
    x = y = 0
    with open("input.txt") as input_file:
        directions = input_file.read().strip().split(",")

    most_distant = 0
    for movement in directions:
        movement = MOVEMENTS[movement]

        x += movement[0]
        y += movement[1]

        most_distant = max(most_distant, path_length(x, y))

    print(int(most_distant))


if __name__ == "__main__":
    main()
