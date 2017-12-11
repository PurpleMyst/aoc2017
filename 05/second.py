#!/usr/bin/env python3


def steps_to_leave(maze):
    pc = 0
    steps = 0

    while True:
        assert pc >= 0

        try:
            value = maze[pc]
        except IndexError:
            return steps

        if value >= 3:
            maze[pc] -= 1
        else:
            maze[pc] += 1

        pc += value
        steps += 1


def main():
    with open("input.txt") as input_file:
        maze = [int(line.strip()) for line in input_file]

    print(steps_to_leave(maze))


if __name__ == "__main__":
    main()
