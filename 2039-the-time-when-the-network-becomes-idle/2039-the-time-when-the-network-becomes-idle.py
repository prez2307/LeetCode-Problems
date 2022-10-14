class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        
        adjGraph = defaultdict(list)
        for src, dest in edges:
            adjGraph[src].append(dest)
            adjGraph[dest].append(src)
        
        distances = [math.inf] * n
        q = deque()
        q.append([0,0])
        seen = set()
        
        while q:
            node, dist = q.popleft()
            distances[node] = dist
            
            for nei in adjGraph[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, dist+1))
        
        res = 0
        
        for node, pat in enumerate(patience):
            if node == 0:
                continue
    
            dist = distances[node]
            roundTrip = dist*2
            
            # do not want to include roundTrip time since
            # server will not resend a message at the same time
            # it receives a message
            divide = (roundTrip-1) // pat
            
            # last time sent
            lastSent = divide*pat
            
            # next time the network is idle is one plus last message received
            res = max(res, lastSent+roundTrip+1)
            
        return res
            
            
        
        
        