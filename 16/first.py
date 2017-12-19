#!/usr/bin/env python3
import collections


def main():
    programs = collections.deque([chr(ord('a') + n) for n in range(16)])

    with open("input.txt") as input_file:
        dance_moves = input_file.read().strip().split(",")

    for dance_move in dance_moves:
        if dance_move.startswith("s"):
            programs.rotate(int(dance_move[1:]))
        elif dance_move.startswith("x"):
            a, b = map(int, dance_move[1:].split("/"))

            tmp = programs[a]
            programs[a] = programs[b]
            programs[b] = tmp
        elif dance_move.startswith("p"):
            a, b = dance_move[1:].split("/")
            a = programs.index(a)
            b = programs.index(b)

            tmp = programs[a]
            programs[a] = programs[b]
            programs[b] = tmp
        else:
            raise ValueError(repr(dance_move))

    print("".join(programs))


if __name__ == "__main__":
    main()
