class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        adjGraph = defaultdict(list)
        
        for src, dest in redEdges:
            adjGraph[src].append((dest, "R"))
        
        for src, dest in blueEdges:
            adjGraph[src].append((dest, "B"))
        
        q = [(0, "G", 0)]
        visited = set()
        #visited.add((0, "G"))
        while q:
            node, color, dist = q.pop(0)
            if ans[node] == -1 or ans[node] > dist:
                ans[node] = dist 
            visited.add((node, color))
            
            for neighbor, neighbor_color in adjGraph[node]:
                if color != neighbor_color and (neighbor, neighbor_color) not in visited:
                    q.append((neighbor, neighbor_color, dist + 1))
        return ans
        