#!/usr/bin/env python3

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)

OPPOSITE_DIRECTIONS = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
}


def main():
    with open("input.txt") as input_file:
        game_map = input_file.read().splitlines()

    for y, line in enumerate(game_map):
        try:
            x = line.index('|')
        except ValueError:
            pass
        else:
            break
    else:
        raise ValueError("No start found!")

    direction = DOWN
    steps = 0

    while True:
        next_x = x + direction[0]
        next_y = y + direction[1]

        try:
            next_cell = game_map[next_y][next_x]
        except IndexError:
            next_cell = None
        else:
            if next_x < 0 or next_y < 0:
                break

        if next_cell is None or next_cell == " ":
            opposite = OPPOSITE_DIRECTIONS[direction]

            for next_direction in ALL_DIRECTIONS:
                if next_direction == direction or next_direction == opposite:
                    continue

                neighbor_x = x + next_direction[0]
                neighbor_y = y + next_direction[1]

                try:
                    neighbor_cell = game_map[neighbor_y][neighbor_x]
                except IndexError:
                    continue
                else:
                    if neighbor_x < 0 or neighbor_y < 0:
                        continue

                if neighbor_cell != ' ':
                    direction = next_direction
                    break
            else:  # no break
                break
        else:
            steps += 1
            x = next_x
            y = next_y

    print(steps + 1)


if __name__ == "__main__":
    main()
