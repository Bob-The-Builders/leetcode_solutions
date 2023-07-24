class Solution:
    def longestPalindrome(self, s: str) -> str:
        biggest_string = ""
        biggestlength = 0
        for i in range(len(s)):
            for j in range(len(s)):
                temp_string = s[i:j + 1]
                if temp_string[::-1] == temp_string and len(temp_string) > biggestlength:
                    biggest_string = temp_string
                    biggestlength = len(biggest_string)
        return biggest_string


    def isPalindrome(self, text: str) -> bool:
        if self.reverseString(text) == text:
            return True
        return False
        
    def reverseString(self, text: str) -> str:
        return text[::-1]
    
x = Solution().longestPalindrome("abb")
print(x)

