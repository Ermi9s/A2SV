# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def findmax(node , maxi):
            if node.left:
                maxi = max(node.left.val , findmax(node.left , maxi))
                
            if node.right:
                maxi = max(node.right.val , findmax(node.right , maxi))
    
            return maxi 

        def findmin(node , mini):
            if node.left:
                mini = min(node.left.val , findmin(node.left , mini))
                
            if node.right:
                mini = min(node.right.val , findmin(node.right , mini))
                
            
            return mini 
        
        diff = 0
        mini = findmin(root , float('inf'))
        maxi = findmax(root , float('-inf'))


        diff = max(abs(root.val - mini ), abs(root.val - maxi))
      
      
        if root.left:
            diff = max(diff ,  self.maxAncestorDiff(root.left))
        if root.right:
            diff = max(diff ,  self.maxAncestorDiff(root.right))
   
        return diff if diff != float('inf') else 0








        