class Solution:
    def isHappy(self, n: int) -> bool:
        seenNumbers: list[int] = []
        temp: int = n
        while(n>0):
            temp = 0
            while(n>0):
                i = n%10
                temp+=i*i
                n=n//10
            if temp in seenNumbers:
                return False
            else:
                seenNumbers.append(temp)
            if (temp==1):
                return True
            n = temp
        return False


    
print(Solution().isHappy(2))