class Solution {
public:
    int minAddToMakeValid(string s) {
        vector<char>stk;

        for(char c : s) {
            if(stk.size() && stk[stk.size()-1] == '(' && c == ')') {
                stk.pop_back();
            }else {
                stk.push_back(c);
            }
        }

        return stk.size();
        
    }
};