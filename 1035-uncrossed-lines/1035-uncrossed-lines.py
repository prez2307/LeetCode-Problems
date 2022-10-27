class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l = len(nums1)
        num1Map = defaultdict(list)
        num2Map = defaultdict(list)
        
        for index, value in enumerate(nums1):
            num1Map[value].append(index)
        
        for index, value in enumerate(nums2):
            num2Map[value].append(index)
            
        @lru_cache(None)
        def helper(idx, threshold):
            if idx >= l:
                return 0
            
            res = helper(idx + 1, threshold)
            num = nums1[idx]
            
            for nextInd in num2Map[num]:
                if nextInd > threshold:
                    res = max(res, helper(idx + 1, nextInd) + 1)
            return res
    
        return helper(0, -1)