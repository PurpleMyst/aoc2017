#!/usr/bin/env python3


def collides(range_, ticks):
    assert range_ > 0

    return (ticks % (2 * (range_ - 1))) == 0


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
            firewall.append(scanners[depth])
        else:
            firewall.append(None)

    delay = 0

    while True:
        for depth, range_ in enumerate(firewall):
            if range_ is None:
                continue

            if collides(range_, delay + depth):
                break
        else:
            print(delay)
            return

        delay += 1


if __name__ == "__main__":
    main()
