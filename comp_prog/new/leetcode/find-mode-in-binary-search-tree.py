# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def traverse(node):
            if node.left:
                traverse(node.left)
            
            count[node.val] += 1

            if node.right:
                traverse(node.right)
        
        traverse(root)

        ans = []

        for i in count.keys():
            temp = [count[i] , i]

            ans.append(temp)
        
        ans.sort(reverse = True)

        rans = []
        rans.append(ans[0][1])
        maxi = ans[0][0]

        for i in range(1 , len(ans)):
            if ans[i][0] == maxi:
                rans.append(ans[i][1])
            else:
                break
        
        return rans


            

        