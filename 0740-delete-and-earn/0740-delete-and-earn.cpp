class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        unordered_map<int , int>count;
        for(auto x : nums) {
            count[x]++;
        }
        vector<int>unique;

        for(int i = 0; i <= 2*pow(10 , 4); i++) {
            unique.push_back(i);
        }

        int dp[unique.size()];

        dp[0] = 0;
        int n = unique.size();

        for(int i = 1; i < n; ++i) {
            if(i == 1){
                dp[i] = max(count[unique[i]]*unique[i] , dp[i-1]);
                continue;
            }
            dp[i] = max(unique[i]*count[unique[i]] + dp[i-2] , dp[i-1]);
        }

        return dp[n-1];

    }
};