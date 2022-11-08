class Solution:
    def equalFrequency(self, word: str) -> bool:
        seen = defaultdict(int)
        for char in word:
            seen[char] += 1
        
        for char in word:
            seen[char] -= 1
            
            if seen[char] == 0:
                seen.pop(char)
            
            if len(set(seen.values())) == 1:
                return True
            
            seen[char] += 1
        
        return False
            