fn row_checksum(row: &str) -> u64 {
    let numbers: Vec<u64> = row.split_whitespace()
                               .map(|n| n.parse().unwrap())
                               .collect();

    for &number in numbers.iter() {
        for &other in numbers.iter() {
            if number != other && number % other == 0 {
                return number / other;
            }
        }
    }

    panic!("at the disco");
}

fn main() {
    let checksum: u64 = include_str!("input.txt").lines().map(row_checksum).sum();

    println!("{}", checksum);
}
