# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
        elif root and not root.left and val < root.val:
            root.left = TreeNode(val)
        elif root and not root.right and val > root.val:
            root.right = TreeNode(val)
        elif root and root.val >= val:
            root.left = self.insertIntoBST(root.left , val)
        elif root and root.val < val:
            root.right = self.insertIntoBST(root.right , val)
    
        return root
        
        
        
        
        

        