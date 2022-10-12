class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        starts = [rides[i][0] for i in range(len(rides))]
        @lru_cache(None)
        def helper(rideIndex):
            if rideIndex == len(rides):
                return 0
            start, end, tip = rides[rideIndex]
            notTakingRide = helper(rideIndex + 1)
            takeRide = 0
            
            index = self.binarySearch(end,starts)
            takeRide = helper(index) + (end - start + tip)
            
            return max(takeRide, notTakingRide)
        return helper(0)

    def binarySearch(self, value: int, starts: List[List[int]]):
        low = 0
        high = len(starts)
        while low < high:
            med = low + (high - low)//2
            if starts[med] >= value:
                high = med
            else:
                low = med + 1
        return low

            
