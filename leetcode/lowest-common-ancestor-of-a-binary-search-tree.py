# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lstp = []
        lstq = []

        def look(node , tree , path):
            if not tree:
                return
            
            path.append(tree.val)
            if node.val == tree.val:
                return 
    
            elif node.val > tree.val:
                look(node,  tree.right , path)      
            elif node.val < tree.val:     
                look(node , tree.left , path)
        
        look(p , root , lstp)
        look(q , root , lstq)

        l = 0
        r = 0
        key = TreeNode()

        while l < len(lstp) and r < len(lstq):
            if lstp[l] == lstq[r]:
                key.val = lstp[l]
            else:
                break
            
            l += 1
            r += 1
        
        return key

        