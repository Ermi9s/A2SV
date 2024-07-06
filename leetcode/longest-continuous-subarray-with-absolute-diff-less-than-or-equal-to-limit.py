class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        incque = deque()
        decque = deque()

        ans = 0
        s = 0
        for i in range(len(nums)):
            while incque and nums[i] < incque[-1][1]:
                incque.pop()
            while decque and nums[i] > decque[-1][1]:
                decque.pop()
            
            incque.append([i , nums[i]])
            decque.append([i , nums[i]])
           
            while incque and decque and (decque[0][1] - incque[0][1]) > limit:
                print(s, i)
                if s == decque[0][0]:
                    decque.popleft()
                if s == incque[0][0]:
                    incque.popleft()

                s += 1

            ans = max(ans , (i - s + 1))

        
        return ans 
    





        