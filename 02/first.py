#!/usr/bin/env python3


def row_difference(row, *, inf=float("inf")):
    maximum, minimum = -inf, inf

    for item in row:
        if item > maximum:
            maximum = item
        if item < minimum:
            minimum = item

    return maximum - minimum


def spreadsheet_checksum(spreadsheet):
    return sum(map(row_difference, spreadsheet))


def main():
    with open("input.txt") as spreadsheet_file:
        spreadsheet = [[int(col) for col in row.split()]
                       for row in spreadsheet_file.read().splitlines()]
    print(spreadsheet_checksum(spreadsheet))


if __name__ == "__main__":
    main()
