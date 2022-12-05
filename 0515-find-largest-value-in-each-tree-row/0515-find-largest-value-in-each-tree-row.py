# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        
        res = []
        
        while q:
            qLen = len(q)
            currentMax = -math.inf
            
            for i in range(qLen):
                node = q.popleft()
                currentMax = max(node.val, currentMax)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            res.append(currentMax)
        
        return res
        