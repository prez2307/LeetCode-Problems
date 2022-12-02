class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        numTriangle = n - 2
        
        @lru_cache(None)
        def dp(left, right):
            if right - left + 1 < 3:
                return 0
    
            res = math.inf
            for k in range(left + 1, right):
                product = values[left] * values[right] * values[k]
                res = min(res, product + dp(left, k) + dp(k, right))
            
            return res
        
        return dp(0, n - 1)
        
        