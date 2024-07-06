class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(n):
            sums = 0
            subs = 1

            for i in nums:
                sums += i
                if sums > n:
                    subs += 1
                    sums = i

            return subs <= k


        l = max(nums)
        r = sum(nums)

        while l <=  r:
            mid = (l+r)//2
            # print(mid)

            if helper(mid):
                ans = mid
                r = mid - 1   
            else:
                l = mid + 1
        return ans
        