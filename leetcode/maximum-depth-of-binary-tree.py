# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dep = [0]
        max_dep = [0]
        if not root:
            return 0
        def count(node , dep , max_dep):
            dep[0] += 1
            if node.left:
                count(node.left , dep , max_dep)
    
            if node.right:
                count(node.right , dep , max_dep)

            max_dep[0] = max(dep[0] , max_dep[0])
            dep[0] -= 1
        
        count(root , dep , max_dep)

        return max_dep[0]
            



        
        