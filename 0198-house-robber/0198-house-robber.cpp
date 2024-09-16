class Solution {
public:
    int rob(vector<int>& nums) {
        int memo[101];
        fill(memo , memo+101 , -1);

        function<int(int)> dp =[&](int ind) -> int {
            if(ind >= nums.size()){
                return 0;
            }

            if(memo[ind] != -1) {
                return memo[ind];
            }

            memo[ind] = max(dp(ind+1) , dp(ind+2) + nums[ind]);

            return memo[ind];
        };

        return dp(0);
    }
};