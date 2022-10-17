class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        sMap = defaultdict(list)
        
        for i, char in enumerate(s):
            sMap[char].append(i)
            
        
        def check(word):
            indexInS = -1
            for wordChar in word:
                if wordChar not in sMap:
                    return False
                next = bisect.bisect_left(sMap[wordChar], indexInS + 1)
                if next >= len(sMap[wordChar]):
                    return False
                
                indexInS = sMap[wordChar][next]
                
                
            return True
        
        ans = 0
        for word in words:
            if check(word):
                ans += 1
        
        return ans
    
    
    