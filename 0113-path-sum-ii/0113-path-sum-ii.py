# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(root, targetSum, prev):
            if not root:
                return None
            
            targetSum -= root.val
            prev.append(root.val)
            if not root.left and not root.right:
                if targetSum == 0:
                    res.append(prev.copy())
            else:
                dfs(root.left, targetSum, prev)
                dfs(root.right, targetSum, prev)
            prev.pop()
        
        dfs(root, targetSum, [])
        return res
                
        
            
            
            