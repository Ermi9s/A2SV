class Solution {
public:
    int hIndex(vector<int>& citations) {
        function<bool(int)> check = [&](int num) -> bool {
            int count = 0;
            for(auto c : citations){
                if(c >= num){
                    count++;
                }
            }

            return count >= num;
        };
        
        int l = 0;
        int r = citations.size()+1;

        while(l+1 < r){
            int mid = l + (r-l)/2;
            if(check(mid)){
                l = mid;
            }else{
                r = mid;
            }
        }

        return l;
    }
};