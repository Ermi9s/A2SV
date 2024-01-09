class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hel = [0 for _ in range(300)]

        for i in nums:
            hel[i] += 1
        
        ans = []
        for i in range(len(hel)):
            if hel[i] != 0:
                for _ in range(hel[i]):
                    ans.append(i) 
        nums.clear()
        nums[:] = ans

        