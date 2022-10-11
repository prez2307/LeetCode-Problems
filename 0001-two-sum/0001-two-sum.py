class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        
        for i, val in enumerate(nums):
            remaining = target - val
            if remaining in maps:
                return [i, maps[remaining]]
            else:
                maps[val] = i
        
        return []