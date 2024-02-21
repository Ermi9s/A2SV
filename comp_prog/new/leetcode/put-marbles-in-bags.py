class Solution:
    def putMarbles(self, nums: List[int], k: int) -> int:
        arr = []

        for i in range(1 , len(nums)):
            arr.append((nums[i] + nums[i-1]))
        
        arr.sort()

        return sum(arr[len(arr) - (k-1):len(arr)])- sum(arr[:k-1])

        