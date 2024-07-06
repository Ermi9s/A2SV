# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ch = defaultdict(list)
        x = [0]
        y = [0]

        def traverse(node , x , y):
            ch[x[0]].append([y[0] , node.val])
            print(node.val , y[0])
            if node.left:
                y[0] += 1
                x[0] -= 1
                traverse(node.left , x , y)
                y[0] -= 1
                x[0] += 1
            
            if node.right:
                y[0] += 1
                x[0] += 1
                traverse(node.right , x , y)
                y[0] -= 1
                x[0] -= 1
            
            
        
        traverse(root ,x , y)
        print(ch)

        for i in ch.keys():
            ch[i].sort()

        key = sorted(ch)
        ans = []
        
        for i in key:
            temp = [c[1] for c in ch[i]]
            ans.append(temp)

        return ans



    

        
        