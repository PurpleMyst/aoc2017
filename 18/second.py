#!/usr/bin/env python3
import collections


class Executor:
    def __init__(self, instructions, program_id):
        self.instructions = instructions
        self.pc = 0
        self.registers = collections.defaultdict(int)
        self.registers["p"] = program_id

        self.partner = None
        self.waiting_for_message = False
        self.queue = collections.deque()
        self.total_sent = 0

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
            self.partner.queue.append(self._get_value(x))
            self.total_sent += 1
        elif mnemonic == "set":
            self.registers[x] = self._get_value(y)
        elif mnemonic == "add":
            self.registers[x] += self._get_value(y)
        elif mnemonic == "mul":
            self.registers[x] *= self._get_value(y)
        elif mnemonic == "mod":
            self.registers[x] %= self._get_value(y)
        elif mnemonic == "rcv":
            if self.queue:
                self.waiting_for_message = False
                self.registers[x] = self.queue.popleft()
            else:
                # Without going to the next instruction.
                self.waiting_for_message = True
                return not self.partner.waiting_for_message

        if mnemonic == "jgz" and self._get_value(x) > 0:
            self.pc += self._get_value(y)
            assert self.pc >= 0
        else:
            self.pc += 1

        return True


def main():
    with open("input.txt") as input_file:
        instructions = [line.strip().split() for line in input_file]

    executor0 = Executor(instructions, 0)
    executor1 = Executor(instructions, 1)

    executor0.partner = executor1
    executor1.partner = executor0

    while True:
        if not executor0.execute_next_instruction():
            break

        if not executor1.execute_next_instruction():
            break

    print(executor1.total_sent)


if __name__ == "__main__":
    main()
