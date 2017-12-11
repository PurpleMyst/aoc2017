use std::collections::HashMap;

type Direction = (isize, isize);

const UP:    Direction = (0, -1);
const DOWN:  Direction = (0, 1);
const LEFT:  Direction = (-1, 0);
const RIGHT: Direction = (1, 0);

fn next_direction(direction: Direction) -> Direction {
    match direction {
        RIGHT => UP,
        UP => LEFT,
        LEFT => DOWN,
        DOWN => RIGHT,
        _ => panic!("Unknown direction!")
    }
}

fn first_larger(target: u64) -> u64 {
    let mut x = 0;
    let mut y = 0;
    let mut value = 1;
    let mut magnitude = 1;
    let mut direction = RIGHT;

    let mut spiral = HashMap::new();
    spiral.insert((0, 0), 1);

    loop {
        for _ in 0..2 {
            for _ in 0..magnitude {
                if value > target {
                    return value;
                }

                x += direction.0;
                y += direction.1;

                value = 0;

                for yc in -1..2 {
                    for xc in -1..2 {
                        if xc == 0 && yc == 0 {
                            continue;
                        }

                        let ny = y + yc;
                        let nx = x + xc;

                        if let Some(neighbor_value) = spiral.get(&(nx, ny)) {
                            value += neighbor_value;
                        }
                    }
                }

                spiral.insert((x, y), value);
            }

            direction = next_direction(direction);
        }

        magnitude += 1;
    }
}

fn main() {
    let target = include_str!("input.txt").trim().parse().unwrap();
    let result = first_larger(target);

    println!("{}", result);
}
