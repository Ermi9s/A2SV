# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        def check(node):
            # print(f"node: {node.val}")
            res = [True , float('-inf') , float('inf'), node.val]

            if not node.left and not node.right:
                res[1] = max(node.val , res[1])
                res[2] = min(node.val , res[2])
                
                # print(res)
        
            if node.left:
                temp = check(node.left)
                res[0] = (node.val > temp[1]) and temp[0]

                res[1] = max(res[1] , temp[1])
                res[1] = max(node.val , res[1])
                #
                res[2] = min(res[2] , temp[2])
                res[2] = min(res[2] , node.val)

                res[3] += temp[3]
             
            if node.right:
                temp = check(node.right)
                res[0] = res[0] and (node.val < temp[2]) and temp[0]
                res[1] = max(res[1] , temp[1])
                res[1] = max(res[1] , node.val)
                #
                res[2] = min(res[2] , temp[2]) 
                res[2] = min(res[2] , node.val)

                res[3] += temp[3]
            
            if res[0]:
                maxi.append(res[3])
                     
            # print(res)
            return res
        
        check(root)
        return max(maxi)