#!/usr/bin/env python3


def row_result(row, *, inf=float("inf")):
    for i, x in enumerate(row):
        for j, y in enumerate(row):
            if i == j:
                continue

            quot, rem = divmod(x, y)

            if rem == 0:
                return quot


def spreadsheet_checksum(spreadsheet):
    return sum(map(row_result, spreadsheet))


def main():
    with open("input.txt") as spreadsheet_file:
        spreadsheet = [[int(col) for col in row.split()]
                       for row in spreadsheet_file.read().splitlines()]
    print(spreadsheet_checksum(spreadsheet))


if __name__ == "__main__":
    main()
