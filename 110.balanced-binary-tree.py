#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        max_depth = {}
     
        def dfs(node):
            if node.left:
                if not dfs(node.left):
                    return False
            if node.right:
                if not dfs(node.right):
                    return False
            
            left = max_depth[node.left] if node.left else 0
            right = max_depth[node.right] if node.right else 0
            
            max_depth[node] = max(left , right) + 1
            
            if abs(left - right) > 1:
                return False

            return True
        
        return dfs(root)
                        
               
    
        
# @lc code=end