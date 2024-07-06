# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findmax(ptr):
            if ptr.right:
                return findmax(ptr.right)
            else:
                return ptr.val
                

        if not root:
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right , key)
        elif root.val > key:
            root.left = self.deleteNode(root.left , key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left and not root.right:
                root = root.left
            elif not root.left and root.right:
                root = root.right
            else:
                maxi = findmax(root.left)
                root.val = maxi
                root.left = self.deleteNode(root.left , maxi)
            
            return root
        
        return root

        