class Solution:
    def arraySign(self, nums: list[int]) -> int:
        total = 1
        for i in nums:
            total = total * i
        return self.signFunc(total)
    def signFunc(self, num: int) -> int: #returns the sign of a number
        if num > 0:
            return 1
        if num < 0: 
            return -1
        if num == 0:
            return 0
        
print(Solution().arraySign([2,4,4]))