class Solution {
public:
    int countBinarySubstrings(string s) {
        int count_one = 0;
        int count_zero = 0;
        int l=0 , ans = 0;    

        for(int r = 0; r < s.size(); ++r) {
            if(count_one && count_zero && s[r] == s[l]) {
                ans += min(count_zero , count_one);

                while(s[l] == s[r]) {
                    ((s[l] == '1')? count_one-- : count_zero--);
                    l++;
                }

            }
            ((s[r] == '1')? count_one++ : count_zero++);
        }
        
        return ans+min(count_zero , count_one);;
    }
};