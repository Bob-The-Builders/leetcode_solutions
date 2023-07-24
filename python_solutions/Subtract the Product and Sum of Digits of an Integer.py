class Solution:
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
