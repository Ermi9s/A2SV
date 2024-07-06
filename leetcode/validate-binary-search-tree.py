# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = [True , float('-inf') , float('inf')]

        def check(node):
            print(f"node: {node.val}")
            res = [True , float('-inf') , float('inf')]
            if not node.left and not node.right:
                res[0] = True
                res[1] = max(node.val , res[1])
                res[2] = min(node.val , res[2])
                print(res)
                return res
        
            if node.left:
                temp = check(node.left)
                res[0] = res[0] and (node.val > temp[1]) and temp[0]

                res[1] = max(res[1] , temp[1])
                res[1] = max(node.val , res[1])

                res[2] = min(res[2] , temp[2])
                res[2] = min(res[2] , node.val)
            
            if node.right:
                temp = check(node.right)
                res[0] = res[0] and (node.val < temp[2]) and temp[0]
                res[1] = max(res[1] , temp[1])
                res[1] = max(res[1] , node.val)

                res[2] = min(res[2] , temp[2]) 
                res[2] = min(res[2] , node.val)
                     
            # print(res)
            return res
        
        return check(root)[0]



       

        