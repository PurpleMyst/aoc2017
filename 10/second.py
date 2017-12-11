#!/usr/bin/env python3


def main():
    data = list(range(256))
    data_size = len(data)

    with open("input.txt") as input_file:
        lengths = [ord(char) for char in input_file.read().strip()]
        lengths.extend([17, 31, 73, 47, 23])

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

        print(format(accumulator, "02x"), end="")
    print()


if __name__ == "__main__":
    main()
