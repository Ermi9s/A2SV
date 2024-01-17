class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ch = defaultdict(int)
        ch[0] += 1
        count = 0
        sums = 0

        for i in nums:
            sums += i
            count += ch[sums-k]
            ch[sums] += 1
            
        
        return count