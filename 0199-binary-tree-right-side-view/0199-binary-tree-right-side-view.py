# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def bfs(node):
            que = deque([node])
            l = 1

            while que:
                curr = que.popleft()
                l -= 1
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                
                if not l and que:
                    l = len(que)
                    ans.append(que[-1].val)
        
        if root:
            ans.append(root.val)
            bfs(root)
        
        return ans

        