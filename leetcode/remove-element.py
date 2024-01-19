class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rp = nums.count(val)
        nums.sort()
        for _ in range(rp):
            nums.remove(val)
        
        return len(nums)

        
        