class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        maxAv = sums/k

        def helper(number):
            return number / k
        for i in range(1,len(nums) - k + 1):
            sums -= nums[i-1]
            sums += nums[i+k-1]
            maxAv = max(helper(sums) , maxAv)

        return maxAv


        
        return maxAv

        