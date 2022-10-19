class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        low = 0
        high = size - 1
        while low < high:
            med = (low + high)//2
            if nums[med] > nums[high]:
                low = med + 1
            else:
                high = med
        
        k = low
        
        low = 0
        high = size -1
        
        while low <= high:
            med = (low + high) // 2
            real = (med + k) % size
            
            if nums[real] == target:
                return real
            if nums[real] > target:
                high = med - 1
            else:
                low = med + 1
        
        return -1