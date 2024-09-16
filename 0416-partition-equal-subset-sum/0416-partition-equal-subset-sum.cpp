class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sums = accumulate(nums.begin() , nums.end() , 0);
        if(sums%2) {
            return false;
        }
        
        map<pair<int , int> , bool>memo;

        function<bool(int, int)> dp = [&](int ind , int target) -> bool {
            if(ind >= nums.size())return false;
            if(target < 0) return false;
            if(target == 0) return true;

            pair<int , int>key = {ind , target};
            if(memo.find(key) != memo.end()) {
                return memo[key];
            }
            memo[key] = dp(ind+1 , target - nums[ind]) || dp(ind+1 , target);

            return memo[key];
        };

        int target = sums/2;

        return dp(0 , target);

    }
};