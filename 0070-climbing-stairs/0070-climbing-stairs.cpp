class Solution {
public:
    int climbStairs(int n) {
        int dp[2];
        if(n == 1) {
            return 1;
        }
        dp[0] = 1;
        dp[1] = 2;

        for(int i = 2; i < n; ++i) {
            int val = dp[0] + dp[1];
            dp[0] = dp[1];
            dp[1] = val;
        }

        return dp[1];
    }
};