const DATA_SIZE: usize = 256;

fn knot_hash(lengths: Vec<usize>) -> Vec<u8> {
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

    let mut dense_hash: Vec<u8> = Vec::with_capacity(16);

    for n in 0..16 {
        let mut accumulator = 0;

        for m in n * 16..n * 16 + 16 {
            accumulator ^= sparse_hash[m];
        }

        dense_hash.push(accumulator as u8);
    }

    return dense_hash;
}

fn main() {
    let mut lengths: Vec<usize> =
        include_str!("input.txt").trim()
                                 .bytes()
                                 .map(|n| n as usize)
                                 .collect();
    lengths.extend_from_slice(&[17, 31, 73, 47, 23]);

    knot_hash(lengths).iter().for_each(|block| {
        print!("{:02x}", block);
    });
    println!("");
}
