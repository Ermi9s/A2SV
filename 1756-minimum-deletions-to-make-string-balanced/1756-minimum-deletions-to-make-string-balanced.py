class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = {
            'a' : 0,
            'b' : 0,
        }

        for i in range(len(s)):
            if s[i] == 'a':
                dp[s[i]] += 1
            else:
                dp[s[i]] = max(dp['a'] , dp['b']) + 1
        
        return len(s) - max(dp['a'] , dp['b'])