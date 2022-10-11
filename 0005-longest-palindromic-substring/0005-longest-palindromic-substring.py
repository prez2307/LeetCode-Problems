class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = s[0]
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i+1)
            curr = max([curr, odd, even], key=lambda x: len(x))
        
        return curr
    
    def expand(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]