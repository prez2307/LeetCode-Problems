class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        
    #Do BFS q has current position on line and whether is last Backward flag in tuple
    #Calculate forward pass first then calculate backwards pass
    
    
        q = collections.deque()
        seen = set()
        ans = 0
        q.append((0, False))
        seen.add((0, False))

        while q:
            l = len(q)
            for _ in range(l):
                curr, isLastBack = q.popleft()

                if curr == x:
                    return ans

                nextPos = curr + a
                if nextPos not in forbidden and nextPos not in seen and nextPos < 6000:
                    q.append((nextPos, False))
                    seen.add((nextPos, False))

                if not isLastBack:
                    nextPos = curr - b
                    if nextPos >= 0 and (nextPos, True) not in seen and nextPos not in forbidden:
                        q.append((nextPos, True))
                        seen.add((nextPos, True))

            ans += 1


        return -1
            
                
                
            
            
            
            
            
            
        
    