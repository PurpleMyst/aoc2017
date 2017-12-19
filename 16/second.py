#!/usr/bin/env python3
import collections


def apply_dance(dance_moves, programs):
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

def main():
    programs = collections.deque([chr(ord('a') + n) for n in range(16)])
    seen = set()

    with open("input.txt") as input_file:
        dance_moves = input_file.read().strip().split(",")

    for _ in range(10 ** 3):
        tprograms = tuple(programs)

        if tprograms in seen:
            cycle_size = len(seen)
            leftover_iterations = 1000000000 % cycle_size

            for _ in range(leftover_iterations):
                apply_dance(dance_moves, programs)

            print("".join(programs))

            return
        else:
            seen.add(tprograms)

        apply_dance(dance_moves, programs)



if __name__ == "__main__":
    main()
