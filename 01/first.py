#!/usr/bin/env python3


def solver(digits):
    digit_amount = len(digits)
    total = 0

    for i, digit in enumerate(digits):
        if i == digit_amount - 1:
            i = -1

        if digit == digits[i + 1]:
            total += int(digit)

    return total


def main():
    with open("input.txt") as input_file:
        print(solver(input_file.read().strip()))


if __name__ == "__main__":
    main()
