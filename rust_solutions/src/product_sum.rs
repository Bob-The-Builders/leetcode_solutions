/* 1281. Subtract the Product and Sum of Digits of an Integer
Given an integer number n, return the difference between the product of its digits and the sum of its digits.*/

pub struct Solution {}

//O(1) Space complexity and O(log(n)) time complexity

impl Solution {
    pub fn subtract_product_and_sum(self, mut n: i32) -> i32 {
        let mut product_of_digits: i32 = 1;
        let mut sum_of_digits: i32 = 0;

        while n != 0 {
            let digit = n % 10;
            product_of_digits *= digit;
            sum_of_digits += digit;
            n /= 10;
        }

        product_of_digits - sum_of_digits
    }
}

/*class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        productOfDigits = 1
        sumOfDigits = 0
        while n != 0:
            digit = n % 10
            productOfDigits = productOfDigits * digit
            sumOfDigits = sumOfDigits + digit
            n = n // 10
        print(productOfDigits)
        return productOfDigits - sumOfDigits

print(Solution().subtractProductAndSum(231))
*/
