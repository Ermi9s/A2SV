class Solution {
public:
    int minimumLength(string s) {
        int count[26];
      

        for(int i = 0; i < s.size(); i++) {
            int ind = s[i] - 'a';
            count[ind] += 1;
        }

        int ans = s.size();

        for(auto num : count) {
            if(num <= 2)continue;
            if(num%2) {
                ans -= (num-1);
            }else {
                ans -= (num-2);
            }
        }

        return ans;
    }
};