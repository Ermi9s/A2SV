# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        def traverse(ans , node):
            ans.append(node.val)
            if node.left:
                traverse(ans , node.left)
            if node.right:
                traverse(ans , node.right)
        
        traverse(ans , root)

        return ans 

        