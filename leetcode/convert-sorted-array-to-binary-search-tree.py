# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(l , r):
            if l > r:
                return 
            if l == r:
                return TreeNode(nums[l])

            mid = (r + l)//2
            root = TreeNode(nums[mid])

            lt = divide(l , mid - 1)
            rt = divide(mid+1 , r)

            root.left = lt
            root.right = rt

            return root
        
        return divide(0 , len(nums)-1)

            

        