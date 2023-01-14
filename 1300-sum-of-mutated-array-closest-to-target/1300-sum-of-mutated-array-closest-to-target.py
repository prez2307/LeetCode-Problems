class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        def helper(candidate):
            summation = 0
            for val in arr:
                if val > candidate:
                    summation += candidate
                else:
                    summation += val
            return abs(target - summation)

        lo = -10**5
        hi = 10**5
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if helper(mid) > helper(mid + 1):
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo