# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [str(node.val)]
            
            res = [str(node.val) + '->' + path for path in dfs(node.left)]
            res += [str(node.val) + '->' + path for path in dfs(node.right)]
            
            return res
        
        return dfs(root)