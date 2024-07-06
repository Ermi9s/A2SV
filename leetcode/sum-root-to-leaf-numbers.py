# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lst = []
        stk = []

        def traverse(node):
            stk.append(str(node.val))
            if node.left:
                traverse(node.left)                    
                stk.pop()
            if node.right:
                traverse(node.right)
                stk.pop()
            
            if not node.left and not node.right:
                lst.append(int(''.join(stk)))
        
        traverse(root)
        return sum(lst)

        