#!/usr/bin/env python3


class Scanner:
    def __init__(self, range_):
        self.range_ = range_

        self._position = 0
        self._going_up = False

    def tick(self):
        if self._going_up:
            self._position -= 1
        else:
            self._position += 1

        if self._position == self.range_ - 1:
            self._going_up = True
        elif self._position == 0:
            self._going_up = False

    def at_top(self):
        return self._position == 0


def main():
    scanners = {}
    total_depth = 0

    with open("input.txt") as input_file:
        for line in input_file:
            depth, range_ = map(int, line.split(":"))
            scanners[depth] = range_
            total_depth = max(total_depth, depth)

    firewall = []

    for depth in range(total_depth + 1):
        if depth in scanners:
            firewall.append(Scanner(scanners[depth]))
        else:
            firewall.append(None)

    me = 0
    severity = 0

    while me <= total_depth:
        if firewall[me] is not None and firewall[me].at_top():
            severity += me * firewall[me].range_

        for scanner in firewall:
            if scanner is not None:
                scanner.tick()

        me += 1

    print(severity)


if __name__ == "__main__":
    main()
