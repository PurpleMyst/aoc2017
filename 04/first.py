#!/usr/bin/env python3


def main():
    with open("input.txt") as input_file:
        counter = 0

        for passphrase in input_file:
            words = passphrase.strip().split()
            seen = set()

            for word in words:
                if word in seen:
                    break
                else:
                    seen.add(word)
            else:  # no break
                counter += 1

        print(counter)


if __name__ == "__main__":
    main()
