class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        length = 0
        ch = defaultdict(int)

        while r < len(s):
            ch[s[r]] += 1
            while l <= r and ch[s[r]] > 1:
                ch[s[l]] -= 1
                l += 1
            
            length = max(length , r - l + 1)
            r += 1
            
        return length

        

        



        