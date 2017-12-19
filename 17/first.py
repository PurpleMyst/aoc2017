#!/usr/bin/env python3


def main():
    with open("input.txt") as input_file:
        skip = int(input_file.read())

    buf = [0]
    buf_size = 1
    pos = 0
    value = 1

    for _ in range(2017):
        pos += skip
        pos %= buf_size
        pos += 1
        buf_size += 1
        buf.insert(pos, value)
        value += 1

    print(buf[pos + 1])


if __name__ == "__main__":
    main()
