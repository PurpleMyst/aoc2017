#!/usr/bin/env python3
# I'm leaving this here for posterity, and for fun.
# I coded a whole A* algorithm (admittedly with help from Wikipedia) before
# realizing that just using the distance() function would've been enough.
# At least if I need a hexagonal A* for any other challenge I have it here =P

import collections
import heapq

# Axial Coordinates are used here.
# See: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
MOVEMENTS = {
    "n": (0, -1),
    "s": (0, +1),

    "ne": (+1, -1),

    "nw": (-1, 0),

    "se": (+1, 0),

    "sw": (-1, +1),
}


def distance(x1, y1, x2, y2):
    return (abs(x1 - x2) +
            abs(x1 + y1 - x2 - y2) +
            abs(y1 - y2)) / 2


def path_length(start, goal):
    g_score = collections.defaultdict(lambda: float("inf"))
    g_score[start] = 0

    f_score = collections.defaultdict(lambda: float("inf"))
    f_score[start] = distance(*start, *goal)

    opened = [(f_score[start], start)]
    closed = set()

    while opened:
        dist, current = heapq.heappop(opened)

        if current == goal:
            return dist

        closed.add(current)

        for dx, dy in MOVEMENTS.values():
            nx = current[0] + dx
            ny = current[1] + dy
            neighbor = (nx, ny)

            if neighbor in closed:
                continue

            if neighbor in f_score:
                continue

            tentative_g_score = \
                g_score[current] + distance(*current, *neighbor)

            if tentative_g_score >= g_score[neighbor]:
                continue

            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = tentative_g_score + distance(*neighbor, *goal)
            heapq.heappush(opened, (f_score[neighbor], neighbor))

    raise LookupError("Could not find a path!")


def main():
    x = y = 0
    with open("input.txt") as input_file:
        directions = input_file.read().strip().split(",")

    for movement in directions:
        movement = MOVEMENTS[movement]

        x += movement[0]
        y += movement[1]

    print(int(path_length((0, 0), (x, y))))


if __name__ == "__main__":
    main()
