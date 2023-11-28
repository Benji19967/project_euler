// Problem 26 -- unsolved

use std::cmp;

fn main() {
    let mut longest_recurring_cycle = 0;

    for i in 2..1000 {
        let curr_length = length_recurring_cycle(i);
        longest_recurring_cycle = cmp::max(longest_recurring_cycle, curr_length);
    }
    println!("{}", longest_recurring_cycle);
}

fn length_recurring_cycle(i: u32) -> u32 {
    let fraction: f64 = 1.0 / i as f64;
    let fraction_str: String = fraction.to_string();

    // Iterate over decimal part (ignore integer part and dot)
    for digit in fraction_str[2..].chars() {
        println!("{}", digit);
    }
    // println!("{}", decimals);
    i
}
