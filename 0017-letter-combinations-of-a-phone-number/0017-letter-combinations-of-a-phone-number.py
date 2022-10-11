class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "}
        
        if len(digits) == 0:
            return []
        
        res = ['']
        
        for digit in digits:
            curr = []
            for letter in digitMapping[digit]:
                for lists in res:
                    curr.append(lists + letter)
            res = curr
        
        return res