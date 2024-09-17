class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string , int>count;
        string word;
        stringstream ss1(s1);
        stringstream ss2(s2);

        while(ss1 >> word) {
            count[word]++;
        }

        while(ss2 >> word) {
            
            count[word]++;
        }

        vector<string>ans;
        stringstream ss3(s1);
        stringstream ss4(s2);

        while(ss4 >> word) {
            if(count[word] == 1){
                ans.push_back(word);
            }
        }

        while(ss3 >> word) {
            if(count[word] == 1){
                ans.push_back(word);
            }
        }

        return ans;

    }
};