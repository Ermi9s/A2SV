class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        nums.sort(reverse=True)
        nums.sort(key=lambda x:d[x])
        return nums