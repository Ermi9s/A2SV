class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int dp[cost.size()+1];
        dp[0] = cost[0];
        dp[1] = cost[1];

        int n = cost.size();
        cost.push_back(0);

        for(int i = 2; i < n+1; ++i) {
            dp[i] = min(dp[i-1] , dp[i-2]) + cost[i];
        }

        return dp[n];
    }
};