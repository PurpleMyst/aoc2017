#!/usr/bin/env python3


def connections(graph, group):
    opened = set()
    closed = set()

    opened.add(group)

    while opened:
        node = opened.pop()

        if node in closed:
            continue
        closed.add(node)

        for neighbor in graph[node]:
            opened.add(neighbor)

    return len(closed)


def main():
    graph = {}

    with open("input.txt") as input_file:
        for line in input_file:
            line = line.strip()
            node, edges = line.split(" <-> ")
            edges = edges.split(", ")
            assert node not in graph
            graph[node] = edges

    print(connections(graph, "0"))


if __name__ == "__main__":
    main()
