class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        l = len(nums)
        left = 0
        minVal = -1
        maxVal = -1
        
        for right, value in enumerate(nums):
            if value > maxK or value < minK:
                left = right + 1
            else:
                if value == minK:
                    minVal = right
                if value == maxK:
                    maxVal = right
                if minVal >= left and maxVal >= left:
                    ans += min(minVal, maxVal) - left + 1
        return ans
            
            