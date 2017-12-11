#!/usr/bin/env python3
import re


ESCAPED_BANGS_REGEXP = re.compile(r"(!!)+")
GARBAGE_REGEXP = re.compile(r"<.*?(?<!!)>")


def remove_garbage(data):
    return GARBAGE_REGEXP.sub("", ESCAPED_BANGS_REGEXP.sub("", data))


def score_groups(data, weight=1):
    groups = []
    score = weight

    for index, char in enumerate(data):
        if char == "{":
            groups.append(index)
        elif char == "}":
            start = groups.pop()
            contents = data[start:index+1]

            if start != 0 and len(groups) == 1:
                score += score_groups(contents, weight + 1)

    assert not groups, "Malformed input!"

    return score


def main():
    with open("input.txt") as input_file:
        data = input_file.read()

    print(score_groups(remove_garbage(data)))


if __name__ == "__main__":
    main()
