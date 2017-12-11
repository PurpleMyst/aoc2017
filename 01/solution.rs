use std::io;

fn main() {
    let mut inp = String::new();
    io::stdin().read_line(&mut inp).expect("Could not read from stdin.");

    let v: Vec<u8> = inp.bytes()
                        .filter(|x| *x >= b'0' && *x <= b'9')
                        .map(|x| x - b'0')
                        .collect();

    let v_len = v.len();
    let half_v_len = v_len / 2;

    let mut part_one: u64 = 0;
    let mut part_two: u64 = 0;

    for (index, &num) in v.iter().enumerate() {
        if num == v[(index + 1) % v_len] {
            part_one += num as u64;
        }

        if num == v[(index + half_v_len) % v_len] {
            part_two += num as u64;
        }
    }

    println!("Part One: {}", part_one);
    println!("Part Two: {}", part_two);
}
