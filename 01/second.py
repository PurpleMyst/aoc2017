#!/usr/bin/env python3


def solver(digits):
    digit_amount = len(digits)
    step_size = digit_amount // 2

    total = 0

    for i, digit in enumerate(digits):
        if digit == digits[(i + step_size) % digit_amount]:
            total += int(digit)

    return total


def main():
    with open("input.txt") as input_file:
        print(solver(input_file.read().strip()))


if __name__ == "__main__":
    main()
