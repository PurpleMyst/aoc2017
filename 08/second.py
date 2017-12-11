#!/usr/bin/env python3
import collections
import re

INSTRUCTION_REGEXP = re.compile(
    r"(\w+) (inc|dec) (-?\d+) if (\w+) ([><!=]=?) (-?\d+)"
)


def condition(x, op, y):
    return eval(f"{x} {op} {y}")


def main():
    registers = collections.defaultdict(int)
    highest_value = 0

    with open("input.txt") as input_file:
        for line in input_file:
            match = INSTRUCTION_REGEXP.match(line)

            if not match:
                raise ValueError(line.strip())

            groups = match.groups()

            if condition(registers[groups[3]], groups[4], groups[5]):
                value = int(groups[2])
                if groups[1] == "dec":
                    value = -value
                registers[groups[0]] += value
                if registers[groups[0]] > highest_value:
                    highest_value = registers[groups[0]]

    print(highest_value)


if __name__ == "__main__":
    main()
