# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sums = 0
        def traverse(node):
            nonlocal sums
            if node.val <= high and node.val >= low:
                sums += node.val
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
                
        traverse(root)
        return sums
        