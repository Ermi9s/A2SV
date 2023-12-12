class Solution(object):
    def twoSum(self, nums, target):
        n = sorted(nums)
        co = len(nums)-1
        i = 0
        j = co 
        lst = []
        
        while i < j:
            if n[i] + n[j] > target:
                j -= 1
            elif n[i] + n[j] < target:
                i += 1
            else:
                lst.append(nums.index(n[i]))
                lst.append((co) - nums[::-1].index(n[j]))
                i+=1
                j-=1
        
        return lst
            
            
                

            
    
       



        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        