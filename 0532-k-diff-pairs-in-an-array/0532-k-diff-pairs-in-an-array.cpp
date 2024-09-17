class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        sort(nums.begin() , nums.end());
        int ans = 0;
        unordered_map<int , bool>found,seen;

        for(auto num : nums) {
            int diff = num - k;
            if(found[diff]){
                ans++;
                found[diff] = false;
                seen[diff] = true;
            }
            if(!seen[num])found[num] = true;
        }
        return ans;
    }
};