#!/usr/bin/env python3
import re


ESCAPED_CHARS_REGEXP = re.compile(r"!.")
GARBAGE_REGEXP = re.compile(r"<(.*?(?<!!))>")


def main():
    with open("input.txt") as input_file:
        data = input_file.read()
    data = ESCAPED_CHARS_REGEXP.sub("", data)

    print(sum(map(len, GARBAGE_REGEXP.findall(data))))


if __name__ == "__main__":
    main()
