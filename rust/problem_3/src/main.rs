use bv::BitVec;

fn main() {
    // Get a number from the user
    let mut largest_num = String::new();
    std::io::stdin()
        .read_line(&mut largest_num)
        .expect("Failed to read line");
    let largest_num: u64 = largest_num
        .trim()
        .parse()
        .expect("Please enter a positive number!");

    // Find it's largest prime factor and print it
    let target_factors: Vec<u64> = factors(largest_num);
    let target_primes: Vec<u64> = prime_filter(target_factors);
    match target_primes.last() {
        Some(prime_result) => println!("Largest Prime Factor: {}", prime_result),
        None => println!("There aren't any prime factors!"),
    }
}

fn factors(target: u64) -> Vec<u64> {
    let mut factor_list = Vec::new();
    for i in 2..target / 2 + 1 {
        if target % i == 0 {
            factor_list.push(i);
        }
    }
    factor_list
}

fn prime_filter(target: Vec<u64>) -> Vec<u64> {
    // Get the largest element
    let max_number_to_check = match target.last() {
        Some(&num) => num,
        None => return Vec::new(),
    };

    // Initialize and set up prime mask
    // Using BitVec for memory efficiency
    let mut prime_mask: BitVec = BitVec::new_fill(true, max_number_to_check);
    prime_mask.set(0, false);
    prime_mask.set(1, false);

    // Generate the whole mask
    const FIRST_PRIME_NUMBER: u64 = 2;
    for p in FIRST_PRIME_NUMBER..max_number_to_check + 1 {
        if prime_mask[p] {
            let mut i = 2 * p;
            while i < max_number_to_check {
                prime_mask.set(i, false);
                i += p;
            }
        }
    }

    // Make a vector of all elements of target which are valid primes
    let mut prime_factors = Vec::new();
    for element in target {
        if prime_mask[element] {
            prime_factors.push(element);
        }
    }
    prime_factors
}
