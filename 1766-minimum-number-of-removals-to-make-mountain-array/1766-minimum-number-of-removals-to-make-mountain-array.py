class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def liss(arr):
            stk = []
           
            for i in range(len(arr)):
                if not stk or (stk[-1] < arr[i]):
                    stk.append(arr[i])
                else:
                    ind = bisect_left(stk , arr[i])
                    stk[ind] = arr[i]
            
    
            return len(arr) - len(stk)
        
        def calc(ind):
            left = []
            cost = 0
            for i in range(ind):
                if nums[i] < nums[ind]:
                    left.append(nums[i])
                else:
                    cost += 1
            
            right = []
            for i in range(len(nums)-1, ind , -1):
                if nums[i] < nums[ind]:
                    right.append(nums[i])
                else:
                    cost += 1

            if not left or not right:
                return False,0

            cost += (liss(left) + liss(right))
            return True,cost


        ans = float('inf')
        for i in range(1 , len(nums)-1):
            ok,cost = calc(i)
            if ok:
                ans = min(ans , cost) 
        
        return ans 





    

            




        