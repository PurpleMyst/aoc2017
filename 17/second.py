#!/usr/bin/env python3


def main():
    with open("input.txt") as input_file:
        skip = int(input_file.read())

    buf_size = 1
    pos = 0
    value = 1
    after_zero = None

    for _ in range(50000000):
        pos += skip
        pos %= buf_size
        pos += 1
        buf_size += 1

        if pos == 1:
            after_zero = value

        value += 1

    print(after_zero)


if __name__ == "__main__":
    main()
