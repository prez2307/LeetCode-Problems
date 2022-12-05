# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, targetSum):
            if not node:
                return False
            
            targetSum -= node.val
            
            if not node.left and not node.right:
                return targetSum == 0
            
            return dfs(node.left, targetSum) or dfs(node.right, targetSum)
        
        return dfs(root, targetSum)
            
            