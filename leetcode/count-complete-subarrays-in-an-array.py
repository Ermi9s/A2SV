class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        l = 0
        r = 0
        ini = len(set(nums))
        base = len(set(nums))
        

        while ini <= len(nums):
            r = ini
            ch = defaultdict(int)
            for i in nums[:r]:
                ch[i] += 1

            for l in range(len(nums) - ini + 1):
                if len(ch) == base:
                    count += 1
    
                if r < len(nums):
                    ch[nums[r]] += 1
                    ch[nums[l]] -= 1

                if ch[nums[l]] < 1:
                    del ch[nums[l]]
                
                r += 1
            
            ini += 1
       

        return count




                

        
            
          
        


        