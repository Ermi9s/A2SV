class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char , int>count,temp;
        if(s1.size() > s2.size()){
            return false;
        }
        function<bool()> check = [&]() -> bool {
            for(int i=0; i < s1.size(); ++i){
                if(count[s1[i]] != temp[s1[i]]){
                    return false;
                }
            }
            return true;
        };

        for(int i=0; i < s1.size(); ++i){
            count[s1[i]]++;
            temp[s2[i]]++;
        }

        if(check()){
            return true;
        }

        int l = 0;
        for(int r = s1.size(); r < s2.size(); ++r){
            temp[s2[r]]++;
            temp[s2[l]]--;
            l++;
            if(check()){
                return true;
            }
        }

        return false;
    }
};