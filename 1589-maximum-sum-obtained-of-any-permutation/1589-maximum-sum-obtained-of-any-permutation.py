class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        l = len(nums)
        prefix = [0] * l
        for start, end in requests:
            prefix[start] += 1
            if end + 1 < l:
                prefix[end + 1] -= 1
            
        for i in range(1,l):
            prefix[i] += prefix[i - 1]
            
        heap = []
        for index, value in enumerate(prefix):
            heappush(heap, (-value, index))
        
        arr = [0] * l
        nums.sort()
        numIndex = l - 1
        
        while heap:
            _, idx = heappop(heap)
            arr[idx] = nums[numIndex]
            numIndex -= 1
        
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        
        res = 0
        for start, end in requests:
            res += arr[end]
            if start > 0:
                res -= arr[start -1]
        return res % (10 **9 + 7)