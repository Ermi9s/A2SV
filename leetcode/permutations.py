class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        def backtrack(nums):
            ans.append(nums)
            seen.add(tuple(nums))
       
            for i in range(len(nums)-1):
                arr = nums[:]
                arr[i],arr[i+1] = arr[i+1],arr[i]
                if tuple(arr) not in seen:
                    backtrack(arr)
        

        backtrack(nums)
        return ans




            


