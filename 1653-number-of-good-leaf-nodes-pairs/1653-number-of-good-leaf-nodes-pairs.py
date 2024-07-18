# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = defaultdict(list)


        def dfs1(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs1(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs1(node.right)
            
        dfs1(root)
        ans = 0
        seen2 = set()

        def bfs(node):
            nonlocal ans,distance,seen2
            que = deque([node])
            seen = set()
            dis = 0
            counter = 1
            while que:
                curr = que.popleft()
                counter -= 1

                # print(curr.val , dis)
                if not curr.left and not curr.right and curr != node:
                    if dis <= distance and (node , curr) not in seen2:

                        ans += 1
                        seen2.add((curr , node))
            
                for nbr in graph[curr]:
                    if nbr not in seen:
                        seen.add(nbr)
                        que.append(nbr)
                
                if counter == 0:
                    dis += 1
                    counter = len(que)
        
        def dfs(node):
            if not node.left and not node.right:
                bfs(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)

        return ans


    
        