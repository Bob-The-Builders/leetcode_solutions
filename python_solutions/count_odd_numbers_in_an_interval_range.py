import math

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        midpoint = (high - low) / 2 #can use // for floor division
        if low % 2 == 0 and high % 2 == 0: #if both are even
            return int(midpoint)
        elif low % 2 == 1 and high % 2 == 1: #if both are odd
            return int(midpoint + 1)
        else: #if only one is odd
            return int(math.ceil(midpoint))
        

#alternative solution
class Solution2:
    def countOdds(self, low: int, high: int) -> int:
        n= (high-low)//2
        if low%2==0 and high%2==0:
            return n
        return n+1 
