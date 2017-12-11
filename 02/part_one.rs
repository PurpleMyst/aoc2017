use std::io::BufRead;

fn row_checksum(row: std::io::Result<String>) -> u64 {
    let numbers: Vec<u64> = row.unwrap()
                               .split_whitespace()
                               .map(|n| n.parse().unwrap())
                               .collect();

    numbers.iter().max().unwrap() - numbers.iter().min().unwrap()
}

fn main() {
    let stdin = std::io::stdin();
    let checksum: u64 = stdin.lock().lines().map(row_checksum).sum();

    println!("Part One: {}", checksum);
}
