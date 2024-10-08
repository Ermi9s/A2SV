class Solution {
public:
    int minSwaps(string s) {
        vector<char>stack;
     
        for(int i = 0; i < s.size(); i++) {
            if(stack.size() && s[i] == ']') {
                stack.pop_back();
            }else{
                stack.push_back(s[i]);
              
            }
        }

    
        return (stack.size()/2);
    }
};