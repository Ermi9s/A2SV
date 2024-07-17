# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        doomed = set(to_delete)
        ans = []
        def dfs(root):
            stk = [(root , 0)]
            while stk:
                node , stat = stk.pop()

                if stat == 1:
                    if node.val in doomed:
                        if node.left and node.left.val not in doomed:
                            ans.append(node.left)
                        if node.right and node.right.val not in doomed:
                            ans.append(node.right)
                    else:
                        if node.left and node.left.val in doomed:
                            node.left = None
                        if node.right and node.right.val in doomed:
                            node.right = None
                    continue

                stk.append((node , 1-stat))
                if node.left:
                    stk.append((node.left , 0))
                if node.right:
                    stk.append((node.right , 0))
        

        dfs(root)
        if root.val not in doomed:
            ans.append(root)
        

        return ans          
            

            