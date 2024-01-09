class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sums = 0
        count = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j != k:
                sums = nums[i] + nums [j] + nums[k]
                pcount = count
                if sums > target:
                    count = min(count,(sums - target))
                else:
                    count = min(count,(target-sums))
        
                if count < pcount:
                    ans = sums
                if count == 0:
                    return sums
                elif sums - target > 0:
                    k -= 1
                else:
                    j += 1
        
        return ans
        
    #nums = [-1,2,1,-4], target = 1
    #i j k 
    # abs(i + j + k) - 1 = min
    # sort >> [-4,-1,1,2]
    # i = -4 j = 1 k = 2
    # i + j + k = -3
    # sl = min(sl,abs(-3)- 1) = 2
    # sl = min(2,0)
    #sl = 0 return
    # sl 
        