class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dic = {0: [], 1:[], 2:[]}
        res = [0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if len(dic[0]) != 0:
                    res[i] = (res[dic[0][-1]] + 1) * 2 - 1
                else:
                    res[i] = 1
                dic[0] = [i]
                
            if nums[i] == 1:
                if len(dic[1]) != 0:
                    res[i] += 2 * res[dic[1][-1]]
                if len(dic[0]) != 0:
                    res[i] += res[dic[0][-1]]
                dic[1] = [i]
                
            if nums[i] == 2:
                if len(dic[2]) != 0:
                    res[i] += 2 * res[dic[2][-1]]
                    
                if len(dic[1]) != 0:
                    res[i] += res[dic[1][-1]]
                    
                dic[2] = [i]
            
            res[i] = res[i] % (10 ** 9 + 7)
            
        if len(dic[2]) == 0:
            return 0
        return res[dic[2][-1]] % (10 ** 9 + 7)
		