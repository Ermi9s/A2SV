class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        function<vector<string>(string , char)> split = [&](string st , char deli) -> vector<string> {
            stringstream ss(st);
            vector<string>result;
            string word;

            while(getline(ss , word , deli)) {
                result.push_back(word);
            }

            return result;
        };

        unordered_map<string , int>count;

        function<void(string , int)> add = [&](string domain , int val) -> void {
            vector<string>spl = split(domain ,'.');
            string t = "";
            for(int i = spl.size()-1; i >= 0; i--) {
                
                if(t!= "" ){
                    t ="." + t;
                    t =spl[i] + t;
                    
                }else{
                    t = spl[i]+t;
                }
                // cout<<t<<endl;
                count[t] += val;
            }
        };

        for(int i = 0; i < cpdomains.size(); ++i) {
            vector<string>spl = split(cpdomains[i] , ' ');
            int val = stoi(spl[0]);
            add(spl[1] , val);
        }

        vector<string>ans;
        for(auto pair : count) {
            string domain = pair.first;
            string val = to_string(pair.second);
            ans.push_back(val+" "+domain);
        }

        return ans;
    }
};