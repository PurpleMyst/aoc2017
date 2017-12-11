fn row_checksum(row: &str) -> u64 {
    let numbers: Vec<u64> = row.split_whitespace()
                               .map(|n| n.parse().unwrap())
                               .collect();

    numbers.iter().max().unwrap() - numbers.iter().min().unwrap()
}

fn main() {
    let checksum: u64 = include_str!("input.txt").lines().map(row_checksum).sum();

    println!("{}", checksum);
}
