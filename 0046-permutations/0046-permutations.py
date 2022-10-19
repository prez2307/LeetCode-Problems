class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            temp = nums.pop(0)
            perms = self.permute(nums)
            
            for lists in perms:
                lists.append(temp)
            
            result.extend(perms)
            nums.append(temp)
        
        return result