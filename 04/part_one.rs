use std::collections::HashSet;

fn is_valid_password(password: &String) -> bool {
    let mut seen = HashSet::new();

    for word in password.split_whitespace() {
        if !seen.insert(word) {
            return false;
        }
    }

    true
}

fn main() {
    println!("{}", include_str!("input.txt").lines()
                                            .map(String::from)
                                            .filter(is_valid_password)
                                            .count());
}
