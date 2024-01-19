class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ch = defaultdict(int)
        ch[0] = 1

        run = 0
        ans = 0
        for i in nums:
            run += i
            ans += ch[run - goal]
            ch[run] += 1
        
        return ans

