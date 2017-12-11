use std::collections::HashSet;

fn is_valid_password(password: &String) -> bool {
    let mut seen = HashSet::new();

    for word in password.split_whitespace() {
        let mut sorted_word: Vec<char> = word.chars().collect();
        sorted_word.sort();

        if !seen.insert(sorted_word) {
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
