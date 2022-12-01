class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        l = len(houses)
        
        @lru_cache(None)
        def helper(left, right, m):
            num = right - left + 1
            if m > num :
                return math.inf
            
            if num == m:
                return 0
            
            if m == 1:
                idx = (right + left) // 2
                med = houses[idx]
                cost = 0
                for i in range(left, right + 1):
                    cost += abs(houses[i] - med)
                return cost
            
            res = math.inf
            for i in range(left, right + 1):
                res = min(res, helper(left, i, 1) + helper(i + 1, right, m-1))
            
            return res
                    
        
        return helper(0, l-1, k)