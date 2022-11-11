class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        l = len(locations)
        
        
        @lru_cache(None)
        def dfs(index, currFuel):
            if currFuel < 0:
                return 0
            
            ans = 0
            if index == finish:
                ans += 1
            
            for idx in range(l):
                if idx != index:
                    fuelRequired = abs(locations[index] - locations[idx])
                    ans = ans + dfs(idx, currFuel - fuelRequired)
            
            return ans
        
        return dfs(start, fuel) % (10**9 + 7)
                    
                    
            
            
            
        
        
        
        
        