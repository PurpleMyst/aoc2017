use std::collections::{HashMap,BTreeSet};

type Graph<'a> = HashMap<&'a str, Vec<&'a str>>;

fn can_reach_zero(graph: Graph) -> usize {
    let mut open = BTreeSet::new();
    let mut closed = BTreeSet::new();

    open.insert("0");
    loop {
        let node = match open.iter().next() {
            Some(n) => n.clone(),
            None => break
        };

        open.remove(node);

        // BTreeSet::insert returns false if the value was already present in the set.
        if !closed.insert(node) {
            continue;
        }

        for neighbor in graph[node].iter() {
            open.insert(neighbor);
        }
    }

    return closed.len();
}

fn main() {
    let graph: Graph = include_str!("input.txt").lines().map(|line| {
        let mut parts = line.trim().split(" <-> ");

        let node = parts.next().unwrap();
        let edges = parts.next().unwrap().split(", ").collect();

        (node, edges)
    }).collect();

    println!("{}", can_reach_zero(graph));
}
