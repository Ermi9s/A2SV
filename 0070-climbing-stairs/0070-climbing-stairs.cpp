class Solution {
public:
    int climbStairs(int n) {
        int prev,curr;
        if(n == 1) {
            return 1;
        }
        prev = 1;
        curr = 2;

        for(int i = 2; i < n; ++i) {
            int val = prev + curr;
            prev = curr;
            curr = val;
        }

        return curr;
    }
};