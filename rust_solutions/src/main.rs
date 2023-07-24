mod product_sum;

use product_sum::Solution;

fn main() {
    let x: Solution = Solution {};
    let result = x.subtract_product_and_sum(234);
    println!("{}", result);
}
