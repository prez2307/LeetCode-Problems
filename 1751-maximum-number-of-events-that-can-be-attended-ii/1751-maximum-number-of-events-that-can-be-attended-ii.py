class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        ans = 0
        starts = [event[0] for event in events]
        
        @lru_cache(None)
        def dfs(idx, eventsLeft, lastEnd):
            if eventsLeft == 0:
                return 0
            if idx == len(events):
                return 0
            
            start, end, value = events[idx]
            
            ans = dfs(idx + 1, eventsLeft, lastEnd)
            
            nxt =  bisect_right(starts, end)
            ans = max(ans, dfs(nxt, eventsLeft - 1, lastEnd+1) + value)
            
            return ans
        
        return dfs(0, k, -1)