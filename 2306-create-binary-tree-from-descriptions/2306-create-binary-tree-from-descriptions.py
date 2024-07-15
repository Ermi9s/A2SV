# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}

        is_parent = defaultdict(lambda : True)
        for par,ch,is_left in descriptions:
            is_parent[ch] = False
            if par not in mp:
                mp[par] = TreeNode(par)

            if ch not in mp:
                mp[ch] = TreeNode(ch)

            parent = mp[par]
            child = mp[ch]

            if is_left:
                parent.left = child
            else:
                parent.right = child
        
        for par,ch,is_left in descriptions:
            if is_parent[par]:
                root = mp[par]
                break
        
        return root


            

                 



        