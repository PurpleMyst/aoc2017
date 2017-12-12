use std::collections::{HashMap,BTreeSet};

type Graph = HashMap<String, Vec<String>>;

fn connections(graph: &Graph, start: &String) -> BTreeSet<String> {
    let mut open = BTreeSet::new();
    let mut closed = BTreeSet::new();

    open.insert(start);
    loop {
        let node = match open.iter().next() {
            Some(n) => n.clone(),
            None => break
        };

        open.remove(node);

        // BTreeSet::insert returns false if the value was already present in the set.
        if !closed.insert(node.clone()) {
            continue;
        }

        for neighbor in graph[node].iter() {
            open.insert(neighbor);
        }
    }

    return closed;
}

fn main() {
    let mut graph: Graph = include_str!("input.txt").lines().map(|line| {
        let mut parts = line.trim().split(" <-> ");

        let node = String::from(parts.next().unwrap());
        let edges = parts.next().unwrap().split(", ").map(String::from).collect();

        (node, edges)
    }).collect();

    let mut group = String::from("0");
    let mut groups = 0;

    loop {
        let group_members = connections(&graph, &group);

        for node in group_members.iter() {
            graph.remove(node);
        }

        groups += 1;
        group = match graph.iter().next() {
            Some((g, _)) => g.clone(),
            None => break
        };
    }

    println!("{}", groups);
}
