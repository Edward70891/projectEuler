fn main() {
    let mut mults: Vec<u32> = Vec::new();

    for current_num in 1..1000 {
        if current_num % 3 == 0 || current_num % 5 == 0 {
            mults.push(current_num);
        }
    }

    let mut total = 0;
    for current_num in mults.iter() {
        total = total + current_num;
    }

    println!("The total is {}", total);
}
