#!/usr/bin/env python3


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


def spiral_position(target):
    assert target >= 1

    x, y = 0, 0
    value = 1
    magnitude = 1
    direction = RIGHT

    while True:
        for _ in range(2):
            for _ in range(magnitude):
                if value == target:
                    return (x, y)

                x += direction[0]
                y += direction[1]
                value += 1

            direction = NEXT_DIRECTION[direction]
        magnitude += 1


def spiral_distance(target):
    x, y = spiral_position(target)
    return abs(x) + abs(y)


def main():
    with open("input.txt") as input_file:
        target = int(input_file.read())

    print(spiral_distance(target))


if __name__ == "__main__":
    main()
