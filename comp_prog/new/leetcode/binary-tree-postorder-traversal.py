# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        def traverse(ans , node):
            if node.left:
                traverse(ans , node.left)
            
            if node.right:
                traverse(ans , node.right)
            ans.append(node.val)
        traverse(ans , root)

        return ans 
        