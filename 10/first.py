#!/usr/bin/env python3


def main():
    data = list(range(256))
    data_size = len(data)

    with open("input.txt") as input_file:
        lengths = map(int, input_file.read().split(","))

    skip_size = 0
    index = 0

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

    print(data[0] * data[1])


if __name__ == "__main__":
    main()
