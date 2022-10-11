class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'[': ']', '{': '}', '(': ')'} 
        
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack or brackets[stack.pop()] != char:
                    return False
        
        return not stack