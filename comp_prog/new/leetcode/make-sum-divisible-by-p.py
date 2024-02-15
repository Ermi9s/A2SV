class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        key = sum(nums) % p

        if key == 0:
            return 0

        pre = [0]
        ch = defaultdict(int)
        ch[0] = 0
        small = len(nums)
        for i in range(len(nums)):
            pre.append((pre[-1] + nums[i])%p)

            if (pre[-1] - key)%p in ch:
                small = min(small , (i+1) - ch[(pre[-1] - key)%p])

            ch[pre[-1]] = i+1
      
        return -1 if small == len(nums) else small
        

        
        



            
        
    
    #[6,9,14,16]
    # 6 , 0 , 5 , 7
    #[16,10,7,2]
    #7 , 1 , 7, 2
    #[3,4,8,10]
    #3 , 4 , 2 , 4