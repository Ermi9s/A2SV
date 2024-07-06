class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 0
        right = max(nums)
        sums = sum(nums)
        def helper(num):
            sums = 0
            for i in nums:
                sums += ceil(i/num)

            return sums

        while left + 1 < right:
            mid = (left+right)//2

            if helper(mid) > threshold:
                left = mid
            else:
                right = mid

        return right 
        
       





        