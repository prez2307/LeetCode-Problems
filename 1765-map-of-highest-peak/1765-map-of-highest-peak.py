class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rowLen = len(isWater)
        colLen = len(isWater[0])
        
        q = collections.deque()
        visited = set()
        
        for i in range(rowLen):
            for j in range(colLen):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    q.append((i,j))
                    visited.add((i,j))
        
        while q:
            row, col = q.popleft()
            for newRow, newCol in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                if newRow < 0 or newRow >= rowLen or newCol < 0 or newCol >= colLen or (newRow, newCol) in visited:
                    continue
                isWater[newRow][newCol] = isWater[row][col] + 1
                q.append((newRow, newCol))
                visited.add((newRow, newCol))
                
        return isWater