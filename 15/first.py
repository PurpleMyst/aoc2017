#!/usr/bin/env python3


def generator_a(starting_value):
    current = starting_value

    while True:
        current = (current * 16807) % 2147483647
        yield current


def generator_b(starting_value):
    current = starting_value

    while True:
        current = (current * 48271) % 2147483647
        yield current


def main():
    a = generator_a(634)
    b = generator_b(301)
    total = 0

    for _ in range(40 * 10 ** 6):
        current_a = next(a) & 0xFFFF
        current_b = next(b) & 0xFFFF

        if current_a == current_b:
            total += 1

    print(total)


if __name__ == "__main__":
    main()
