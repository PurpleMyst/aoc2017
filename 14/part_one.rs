const DATA_SIZE: usize = 256;

fn popcnt_knot_hash(key: String) -> u32 {
    let mut lengths: Vec<_> = key.trim()
                                 .bytes()
                                 .map(|n| n as usize)
                                 .collect();
    lengths.extend_from_slice(&[17, 31, 73, 47, 23]);

    let mut sparse_hash: Vec<u16> = (0..DATA_SIZE as u16).collect();

    let mut current_position = 0;
    let mut skip_size = 0;

    for _ in 0..64 {
        for length in lengths.iter() {
            let sublist: Vec<_> =
                (current_position..current_position + length).map(|i| sparse_hash[i % DATA_SIZE])
                                                             .rev()
                                                             .collect();

            let mut i = current_position;
            for n in sublist.iter() {
                sparse_hash[i % DATA_SIZE] = *n;
                i += 1;
            }

            current_position += length + skip_size;
            skip_size += 1;
        }
    }

    let mut popcnt = 0;

    for n in 0..16 {
        let mut accumulator = 0;

        for m in n * 16..n * 16 + 16 {
            accumulator ^= sparse_hash[m];
        }

        popcnt += accumulator.count_ones();
    }

    return popcnt;
}

fn main() {
    let mut base_key = include_str!("input.txt").trim().to_owned();
    base_key.push('-');

    let total: u32 = (0..128 as u32).map(|y: u32| {
        let key = base_key.clone() + &y.to_string();
        popcnt_knot_hash(key)
    }).sum();

    println!("{}", total);
}
