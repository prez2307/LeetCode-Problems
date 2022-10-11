class Solution:
    def myAtoi(self, s: str) -> int:
        myString = s.strip()
        digits = list(myString)
        
        sign = 1
        
        if len(digits) == 0: return 0
        if digits[0] == '-':
            sign = -1
        
        if digits[0] in '+-':
            digits = digits[1:]
            
        ans = 0
        
        for val in digits:
            if not val.isdigit():
                break
            ans = ans* 10 + int(val)
        
        return max(-2**31, min(sign * ans, 2**31 - 1))