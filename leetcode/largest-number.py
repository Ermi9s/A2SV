class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compa(a , b):
            first = int(str(a) + str(b))
            second = int(str(b) + str(a))

            if second > first:
                return True

            return False
        
        for i in range(len(nums)-1 , -1 , -1):
            for j in range(i):
                if compa(nums[j] , nums[j+1]):
                    nums[j] , nums[j+1] = nums[j + 1] , nums[j]
    
        ans = []
        for i in range(len(nums)):
            ans.append(str(nums[i]))

        anst = "".join(ans)
        temp = int(anst)

        return str(temp)


        
        
