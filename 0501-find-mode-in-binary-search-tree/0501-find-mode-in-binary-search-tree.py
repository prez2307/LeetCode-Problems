# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        myMap = defaultdict(int)
        
        def dfs(node):
            if not node:
                return
            myMap[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        mymax = max(myMap.values())
        return [k for k,v in myMap.items() if v == mymax]                
                