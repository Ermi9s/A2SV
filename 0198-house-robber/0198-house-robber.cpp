class Solution {
public:
    int rob(vector<int>& nums) {
        int prev = 0;
        int curr = 0;

        for(int i = 0; i < nums.size(); ++i) {
            int val = max(nums[i]+prev , curr);
            prev = curr;
            curr = val;
        }

        return curr;
    }
};