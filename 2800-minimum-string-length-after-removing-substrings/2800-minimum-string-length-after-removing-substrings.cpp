class Solution {
public:
    int minLength(string s) {
        vector<char>stack;

        for(int i = 0; i < s.size(); i++) {
            if(stack.size()) {
                if(stack[stack.size()-1] == 'A' && s[i] == 'B') {
                    stack.pop_back();
                }else if(stack[stack.size()-1] == 'C' && s[i] == 'D') {
                    stack.pop_back();
                }else {
                    stack.push_back(s[i]);
                }
            }else{
                stack.push_back(s[i]);
            }
        }

        return stack.size();
    }
};