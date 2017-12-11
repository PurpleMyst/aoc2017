#!/usr/bin/env python3
import collections

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

NEXT_DIRECTION = {
    RIGHT: UP,
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT
}


def first_larger(target):
    x, y = 0, 0
    value = 1
    magnitude = 1
    direction = RIGHT

    values = collections.defaultdict(int)
    values[x, y] = value

    while True:
        for _ in range(int(magnitude)):
            if value > target:
                return value

            x += direction[0]
            y += direction[1]

            value = 0
            for xc in range(-1, 2):
                for yc in range(-1, 2):
                    if xc == 0 and yc == 0:
                        continue

                    nx, ny = x + xc, y + yc
                    value += values[nx, ny]

            values[x, y] = value

        direction = NEXT_DIRECTION[direction]
        magnitude += 0.5


def main():
    with open("input.txt") as input_file:
        target = int(input_file.read())

    print(first_larger(target))


if __name__ == "__main__":
    main()
