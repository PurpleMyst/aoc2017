fn main() {
    let mut jumps: Vec<isize> =
        include_str!("input.txt").lines().map(|n| n.parse().unwrap()).collect();
    let mut pc: isize = 0;
    let mut steps = 0;

    let jump_amount = jumps.len() as isize;

    loop {
        if pc < 0 || pc >= jump_amount {
            break;
        }

        let value = jumps[pc as usize];
        if value >= 3 {
            jumps[pc as usize] -= 1;
        } else {
            jumps[pc as usize] += 1;
        }

        pc += value;

        steps += 1;
    }

    println!("{}", steps);
}
