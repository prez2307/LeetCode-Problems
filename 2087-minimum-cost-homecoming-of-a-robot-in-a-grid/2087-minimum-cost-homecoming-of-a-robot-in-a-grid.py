class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0
        row = homePos[0]
        col = homePos[1]
        
        while row != startPos[0]:
            ans += rowCosts[row]
            row += -1 if row > startPos[0] else 1
            
        while col != startPos[1]:
            ans += colCosts[col]
            col += -1 if col > startPos[1] else 1
        return ans
        