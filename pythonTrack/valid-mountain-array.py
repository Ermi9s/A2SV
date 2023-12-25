class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        tip = arr[0]
        ind = 0
        right = False
        left = False

        for i, n in enumerate(arr):
            if n > tip:
                tip = n
                ind = i

        if len(arr) < 3 or ind == len(arr) - 1 or ind == 0:
            return False

        for i in range(ind):
            if arr[i] >=  arr[i+1]:
                
                break
        else:
            left = True


        for i in range(ind,len(arr) -1):
            if arr[i] <=  arr[i+1]:
                break 
        else:
            right = True


        return left and right     

        