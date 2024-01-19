class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mul = [0] * (len(nums) + 1)

        for q in requests:
            mul[q[0]] += 1
            mul[q[1] + 1] -= 1
        
        for i in range(1 , len(mul)):
            mul[i] += mul[i-1]
        
        mul.sort(reverse = True)
        nums.sort(reverse = True)

        ans = 0

        for i in range(len(nums)):
            ans += (mul[i] * nums[i])
        
        return ans % (pow(10 , 9) + 7)
        
        
        