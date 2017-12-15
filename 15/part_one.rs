fn next_generator_a(last_value: u64) -> u64 {
    return (last_value * 16807) % 2147483647;
}

fn next_generator_b(last_value: u64) -> u64 {
    return (last_value * 48271) % 2147483647;
}

fn main() {
    let mut a_value = 634;
    let mut b_value = 301;
    let mut total = 0;

    for _ in 0..40_000_000 {
        a_value = next_generator_a(a_value);
        b_value = next_generator_b(b_value);

        if a_value & 0xFFFF == b_value & 0xFFFF {
            total += 1;
        }
    }

    println!("{}", total);
}
