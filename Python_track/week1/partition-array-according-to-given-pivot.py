class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left_side = []
        right_side = []
        equals = []

        for i in nums:
            if i < pivot:
                left_side.append(i)
            elif i > pivot:
                right_side.append(i)
            else:
                equals.append(i)
        
        return left_side + equals + right_side
        