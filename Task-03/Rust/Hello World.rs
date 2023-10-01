use std::io;
fn Prime(n: u32) -> bool {
    if n <= 1 {
        return false;
    }
    if n <= 3 {
        return true;
    }
    if n % 2 == 0 || n % 3 == 0 {
        return false;
    }
    let mut i = 5;
    while i * i <= n {
        if n % i == 0 || n % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }
    true
}

fn main() {
    let mut input = String::new();
    println!("Enter a value for N: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input = input.trim();

    if input.is_empty() {
        println!("Input is empty. Please enter a valid number.");
        return;
    }

    let n: u32 = match input.parse() {
        Ok(num) if num > 1 => num,
        _ => {
            println!("Invalid input. N must be an integer greater than 1.");
            return;
        }
    };

    println!("Prime numbers up to {} are:", n);
    for i in 2..=n {
        if Prime(i) {
            print!("{} ", i);
        }
    }
    println!();
}
