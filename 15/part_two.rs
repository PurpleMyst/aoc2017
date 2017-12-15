fn next_generator_a(mut last_value: u64) -> u64 {
    loop {
        last_value = (last_value * 16807) % 2147483647;

        if last_value & 3 == 0 {
            return last_value;
        }
    }
}

fn next_generator_b(mut last_value: u64) -> u64 {
    loop {
        last_value = (last_value * 48271) % 2147483647;

        if last_value & 7 == 0 {
            return last_value;
        }
    }
}

fn main() {
    let mut a_value = 634;
    let mut b_value = 301;
    let mut total = 0;

    for _ in 0..5_000_000 {
        a_value = next_generator_a(a_value);
        b_value = next_generator_b(b_value);

        if a_value & 0xFFFF == b_value & 0xFFFF {
            total += 1;
        }
    }

    println!("{}", total);
}
