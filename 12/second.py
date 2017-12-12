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

    return closed


def main():
    graph = {}

    with open("input.txt") as input_file:
        for line in input_file:
            line = line.strip()
            node, edges = line.split(" <-> ")
            edges = edges.split(", ")
            assert node not in graph
            graph[node] = edges

    groups = 0
    group = "0"

    while graph:
        group_members = connections(graph, group)

        for member in group_members:
            del graph[member]

        groups += 1
        if graph:
            group = next(iter(graph.keys()))

    print(groups)


if __name__ == "__main__":
    main()
