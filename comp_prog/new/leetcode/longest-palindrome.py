class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        flag = True
        for key, val in count.items():
            if val % 2 == 0:
                ans += val
                count[key] -= val
            else:
                ans += val - 1
                count[key] -= (val - 1)
        
        for i in count.keys():
            if count[i] == 1:
                ans += 1
                break
        

        
        return ans



        