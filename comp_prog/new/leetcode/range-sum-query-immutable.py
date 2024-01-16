class NumArray:

    def __init__(self, nums: List[int]):
        self.cm =[nums[0]]

        for i in range(1 , len(nums)):
            self.cm.append(self.cm[-1] + nums[i])
        self.cm.append(0)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.cm[right] - self.cm[left - 1]


        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)