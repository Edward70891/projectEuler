fn main() {
    let mut fib = vec![1, 2];
    let mut even_fib = vec![2];
    let mut current_num: u32 = fib.iter().sum();

    while current_num < 4_000_000 {
        if current_num % 2 == 0 {
            even_fib.push(current_num);
        }
        fib.push(current_num);

        current_num = fib.iter()
            .rev().take(2).sum();
    }

    let total: u32 = even_fib.iter().sum();

    println!("The sum of the evens is {}", total);
}
