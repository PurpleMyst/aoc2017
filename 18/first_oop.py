#!/usr/bin/env python3
import collections


class Executor:
    def __init__(self, instructions):
        self.instructions = instructions
        self.pc = 0
        self.registers = collections.defaultdict(int)
        self.recovered_frequency = None

    def _get_value(self, argument):
        try:
            return int(argument)
        except ValueError:
            return self.registers[argument]

    def execute_next_instruction(self):
        try:
            instruction = self.instructions[self.pc]
        except IndexError:
            return False

        try:
            mnemonic, x, y = instruction
        except ValueError:
            mnemonic, x = instruction
            y = None

        if mnemonic == "snd":
            self.recovered_frequency = self._get_value(x)
        elif mnemonic == "set":
            self.registers[x] = self._get_value(y)
        elif mnemonic == "add":
            self.registers[x] += self._get_value(y)
        elif mnemonic == "mul":
            self.registers[x] *= self._get_value(y)
        elif mnemonic == "mod":
            self.registers[x] %= self._get_value(y)
        elif mnemonic == "rcv":
            print(self.recovered_frequency)
            exit(0)

        if mnemonic == "jgz" and self._get_value(x) > 0:
            self.pc += self._get_value(y)
            assert self.pc >= 0
        else:
            self.pc += 1

        return True


def main():
    with open("input.txt") as input_file:
        instructions = [line.strip().split() for line in input_file]

    executor = Executor(instructions)
    while True:
        executor.execute_next_instruction()


if __name__ == "__main__":
    main()
