class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start = []
        end = []
        for i in range(len(flowers)):
            start.append(flowers[i][0])
            end.append(flowers[i][1])
        start.sort()
        end.sort()
        ans = []
        
        for person in persons:
            numFlowersBloom = bisect.bisect_right(start, person)
            numFlowersWilt = bisect.bisect_left(end, person)
            ans.append(numFlowersBloom - numFlowersWilt)
        return ans
            