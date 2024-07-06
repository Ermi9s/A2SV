class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        def search(num , l , r):
            while l+1 < r:
                mid = (l+r)//2

                if nums[mid] <= num:
                    l = mid
                else:
                    r = mid
            
            return l
        
        ans = 0
        for l in range(len(nums)):
            key = target - nums[l]
            # print(l)
            # print(search(key , l , len(nums)))
            # print("___")
            k = (search(key , l , len(nums)) - l)
            if k > 0:
                ans += pow(2 , k)
            elif 2*nums[l] <= target:
                ans += 1
        
        return (ans%(10**9 + 7))



        