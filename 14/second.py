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

    used_squares = set()
    for row in range(128):
        lengths = [ord(c) for c in key + "-" + str(row)]
        lengths.extend([17, 31, 73, 47, 23])

        x = 0
        for block in knot_hash(lengths):
            for shift in range(7, -1, -1):
                if block & (0b1 << shift):
                    used_squares.add((x, row))
                x += 1

    regions = 0
    while used_squares:
        opened = {used_squares.pop()}
        closed = set()

        while opened:
            node = x, y = opened.pop()

            if node in closed:
                continue
            else:
                closed.add(node)

            for yc in range(-1, 2):
                for xc in range(-1, 2):
                    if xc == 0 and yc == 0:
                        continue

                    if xc != 0 and yc != 0:
                        continue

                    neighbor = (x + xc, y + yc)

                    if neighbor in used_squares:
                        opened.add(neighbor)

        used_squares -= closed
        regions += 1

    print(regions)


if __name__ == "__main__":
    main()
