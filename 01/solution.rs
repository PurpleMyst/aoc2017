fn main() {
    let v: Vec<u8> = include_str!("input.txt").trim()
                                              .bytes()
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
