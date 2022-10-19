class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:    
        res = []
        freeDays = []
        filled = {}

        for day, city in enumerate(rains):
            if city == 0:
                res.append(1)
                freeDays.append(day)
            else:
                res.append(-1)
                if city not in filled:
                    filled[city] = day
                else:
                    if len(freeDays) > 0 and freeDays[-1] > filled[city]:
                        dry = bisect.bisect_left(freeDays, filled[city])
                        res[freeDays.pop(dry)] = city
                        filled[city] = day
                    else:
                        return []

        return res