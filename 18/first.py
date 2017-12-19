#!/usr/bin/env python3
import collections


def main():
    registers = collections.defaultdict(int)
    pc = 0
    recovered_frequency = None

    def get_value(x):
        try:
            return int(x)
        except ValueError:
            return registers[x]

    with open("input.txt") as input_file:
        instructions = [line.strip().split() for line in input_file]

    while True:
        try:
            instruction = instructions[pc]
        except IndexError:
            break
        else:
            assert pc >= 0

        try:
            mnemonic, x, y = instruction
        except ValueError:
            mnemonic, x = instruction
            y = None

        if mnemonic == "snd":
            recovered_frequency = get_value(x)
        elif mnemonic == "set":
            registers[x] = get_value(y)
        elif mnemonic == "add":
            registers[x] += get_value(y)
        elif mnemonic == "mul":
            registers[x] *= get_value(y)
        elif mnemonic == "mod":
            registers[x] %= get_value(y)
        elif mnemonic == "rcv":
            print(recovered_frequency)
            return

        if mnemonic == "jgz" and get_value(x) > 0:
            pc += get_value(y)
            continue

        pc += 1


if __name__ == "__main__":
    main()
