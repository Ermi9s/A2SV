class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def flip(nums , r):
            left = nums[:r+1][::-1]
            right = nums[r+1:]

            return left + right


        ans = []
        for i in range(len(arr),0,-1):
            maxi = i
            k = arr.index(i)
            arr[:] = flip(arr,k)

            ans.append(k + 1)
            arr = flip(arr,i-1)
            ans.append(i)
            

        return ans
            

      
        
        