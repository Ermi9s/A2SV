class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []

        ch = { i : -1 for i in nums1}

        for i in nums2:
            while stk and stk[-1] < i:
                temp = stk.pop()

                if temp in ch:
                    ch[temp] = i
            
            if (stk and stk[-1] > 1) or not stk:
                stk.append(i)
        
        for i in range(len(nums1)):
            nums1[i] = ch[nums1[i]]
        
        return nums1
            

        
        
        