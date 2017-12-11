use std::io::BufRead;

fn row_checksum(row: std::io::Result<String>) -> u64 {
    let numbers: Vec<u64> = row.unwrap()
                               .split_whitespace()
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
    let stdin = std::io::stdin();
    let checksum: u64 = stdin.lock().lines().map(row_checksum).sum();

    println!("Part Two: {}", checksum);
}
