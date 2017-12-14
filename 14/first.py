#!/usr/bin/env python3


def knot_hash(lengths, data_size=256):
    data = list(range(data_size))

    skip_size = 0
    index = 0

    for _ in range(64):
        for length in lengths:

            sublist = []
            for j in range(index, index + length):
                sublist.append(data[j % data_size])
            sublist.reverse()

            sublist = iter(sublist)
            for j in range(index, index + length):
                data[j % data_size] = next(sublist)

            index += length + skip_size
            skip_size += 1

    for j in range(0, data_size, 16):
        accumulator = 0

        for k in range(j, j + 16):
            accumulator ^= data[k]

        yield accumulator


def main():
    with open("input.txt") as input_file:
        key = input_file.read().strip()
    total = 0

    for row in range(128):
        lengths = [ord(c) for c in key + "-" + str(row)]
        lengths.extend([17, 31, 73, 47, 23])

        for block in knot_hash(lengths):
            while block:
                total += block & 0b1
                block >>= 1

    print(total)


if __name__ == "__main__":
    main()
