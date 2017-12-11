#!/usr/bin/env python3


def steps_to_leave(maze):
    pc = 0
    maze_size = len(maze)
    steps = 0

    while pc >= 0 and pc < maze_size:
        maze[pc] += 1
        pc += maze[pc] - 1
        steps += 1

    return steps


def main():
    with open("input.txt") as input_file:
        maze = [int(line.strip()) for line in input_file]

    print(steps_to_leave(maze))


if __name__ == "__main__":
    main()
