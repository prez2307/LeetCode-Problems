class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0

        maxSoFar = -math.inf
        minSoFar = math.inf

        for i, val in enumerate(nums):
            maxSoFar = max(maxSoFar, val)
            if val < maxSoFar:
                right = i
        
        for i in range(len(nums) - 1, -1, -1):
            val = nums[i]
            minSoFar = min(minSoFar, nums[i])
            if nums[i] > minSoFar:
                left = i

        if right > 0:
            return right - left + 1
        else:
            return 0