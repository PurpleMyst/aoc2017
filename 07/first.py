#!/usr/bin/env python3


def parse_input(input_file):
    programs = {}

    for line in input_file:
        line = line.strip()

        name, weight, *rest = line.split()

        programs.setdefault(name, None)

        if rest:
            arrow = rest.pop(0)
            assert arrow == "->"

            for child in rest:
                child = child.strip(",")
                assert programs.get(child) is None
                programs[child] = name

    return programs


def find_bottom(programs):
    for name, parent in programs.items():
        if parent is None:
            return name


def main():
    with open("input.txt") as input_file:
        programs = parse_input(input_file)

    print(find_bottom(programs))


if __name__ == "__main__":
    main()
