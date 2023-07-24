class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            if n%2 == 1:
                count +=1
            n = n >> 1
        return count
    
#such a cool soltuion, if integer ends in an 0 it's even so we no it's not a 1, then we just bitwise shift the number and deal with the next integer
print(Solution().hammingWeight(11011101))