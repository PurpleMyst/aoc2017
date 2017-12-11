type Point     = (isize, isize);
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

fn spiral_position(target: u64) -> Point {
    let mut x = 0;
    let mut y = 0;
    let mut value = 1;
    let mut magnitude = 1;
    let mut direction = RIGHT;

    loop {
        for _ in 0..2 {
            for _ in 0..magnitude {
                if value == target {
                    return (x, y);
                }

                x += direction.0;
                y += direction.1;
                value += 1;
            }

            direction = next_direction(direction);
        }

        magnitude += 1;
    }
}

fn main() {
    let target = include_str!("input.txt").trim().parse().unwrap();
    let (x, y) = spiral_position(target);
    println!("{}", x.abs() + y.abs());
}
