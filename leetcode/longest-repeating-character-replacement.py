class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch = defaultdict(int)

        r = 0
        l = 0
        ans = 0
        while r<len(s):
            ch[s[r]] += 1

            while (r - l + 1) - max(ch.values()) > k:
                 ch[s[l]] -= 1
                 
                 l += 1
            ans = max(ans , r - l + 1)
            r += 1
        
        return ans
        

        