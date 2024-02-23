class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec = deque()

        for i in range(k):
            while dec and dec[-1][0] < nums[i]:
                dec.pop()
            dec.append([nums[i], i])
        
        ans = [dec[0][0]]

        
        
        for i in range(k , len(nums)):
            if dec and i - dec[0][1] == k:
                dec.popleft()

            while dec and dec[-1][0] < nums[i]:
                dec.pop()
            dec.append([nums[i] , i])
            ans.append(dec[0][0]) 
        
        return ans
        
        