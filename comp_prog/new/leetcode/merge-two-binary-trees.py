# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
       
        def merge(node1 , node2):
            if not node2:
                return 


            node1.val += node2.val

            if node1.left: 
                merge(node1.left , node2.left)
            else:
                node1.left = node2.left

            if node1.right: 
                merge(node1.right , node2.right)
            else:
                node1.right = node2.right
                

        if root1: 
            merge(root1 , root2)
        else:
            root1 = root2
            
        return root1
        