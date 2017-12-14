const DATA_SIZE: usize = 256;

fn knot_hash(lengths: Vec<usize>) -> u16 {
    let mut data: Vec<u16> = (0..DATA_SIZE as u16).collect();

    let mut current_position = 0;
    let mut skip_size = 0;

    for length in lengths.iter() {
        let sublist: Vec<_> =
            (current_position..current_position + length).map(|i| data[i % DATA_SIZE])
                                                         .rev()
                                                         .collect();

        let mut i = current_position;
        for n in sublist.iter() {
            data[i % DATA_SIZE] = *n;
            i += 1;
        }

        current_position += length + skip_size;
        skip_size += 1;
    }

    return data[0] * data[1];
}

fn main() {
    let lengths: Vec<usize> =
        include_str!("input.txt").trim()
                                 .split(",")
                                 .map(|n| n.parse().unwrap())
                                 .collect();

    println!("{}", knot_hash(lengths));
}
