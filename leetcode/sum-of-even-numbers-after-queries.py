class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even = lambda a: a%2==0
        evenSum = sum(filter(even , nums))
        ans = []
        for n,i in queries:
            if nums[i] % 2 == 0:
                evenSum -= nums[i]
            nums[i] += n
            if nums[i] % 2 == 0:
                evenSum += nums[i]
            ans.append(evenSum)
            
        return ans
        