# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        pathQue = deque(traversal)

        def getVal(path, depth):
            for _ in range(depth):
                path.popleft()
            val = ''
            while path:
                if path[0].isdigit():
                    val += path.popleft()
                elif path[0] == '-':
                    break
            return int(val)

        def dfs(path, depth):
            if not path:
                return None
            if depth and not all(path[i] == '-' for i in range(depth)):
                return None
            curVal = getVal(path, depth)
            node = TreeNode(val=curVal)
            node.left = dfs(path, depth+1)
            node.right = dfs(path, depth+1)
            return node

        return dfs(pathQue, 0)