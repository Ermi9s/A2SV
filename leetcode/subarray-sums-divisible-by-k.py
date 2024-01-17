class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ch = defaultdict(int)
        ch[0] += 1
        sums = 0
        count = 0
        for i in nums:
            sums += i
            if sums%k in ch:
                count += ch[sums%k]

            ch[sums%k] += 1

        return count