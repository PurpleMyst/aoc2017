#!/usr/bin/env python3


def max_with_index(iterable):
    return max((x, -i) for i, x in enumerate(iterable))


def steps_until_stuck(memory):
    seen = set()
    memory_size = len(memory)

    while True:
        tmemory = tuple(memory)
        if tmemory in seen:
            return len(seen)
        else:
            seen.add(tmemory)

        blocks_left, offset = max_with_index(memory)

        offset = -offset
        memory[offset] = 0

        offset += 1
        while blocks_left:
            if offset == memory_size:
                offset = 0

            memory[offset] += 1

            blocks_left -= 1
            offset += 1


def main():
    with open("input.txt") as input_file:
        memory = list(map(int, input_file.read().split()))

    print(steps_until_stuck(memory))


if __name__ == "__main__":
    main()
