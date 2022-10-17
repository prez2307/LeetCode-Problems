class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left = 0
        right = len(removable) + 1
        remove = {r : i for i, r in enumerate(removable)}
        
        def checkSubsequence(index):
            i = 0
            j = 0
            while i < len(s) and j < len(p):
                if i in remove and remove[i] <= index:
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(p)
        
        
        while left < right:
            mid = (left + right) // 2
            if checkSubsequence(mid):
                left = mid + 1
            else:
                right = mid
                
        if left < len(removable):
            return left
        else:
            return left-1
    