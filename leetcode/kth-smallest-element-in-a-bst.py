# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = [0]
        save = [0]
        found = [False]

        def find(node , save , n , found):
            if not found[0] and node.left:
                find(node.left , save , n , found)
           
            n[0] += 1
            if n[0] == k:
                found[0] = True
                save[0] = node.val

            if not found[0] and node.right:
                find(node.right , save , n , found)
        
        find(root , save , n , found)
        return save[0]

        

            
            
        