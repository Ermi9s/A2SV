class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # indi = defaultdict(list)
        # big = [0 for _ in range(101)]

        # for i,n in enumerate(nums):
        #     indi[n].append(i)
        
        # for i in nums:
        #     big[i] += 1
        
        # nums.clear()
        # for i,n in enumerate(big):
        #     if n > 0:
        #         for _ in range(n):
        #             nums.append(i)
        ans = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        
        return ans




        
        