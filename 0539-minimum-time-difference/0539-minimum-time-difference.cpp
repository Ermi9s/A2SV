class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int timeline[1440];
        function<int(string)> convert = [&](string time) -> int {
            int first;
            int offset;
            if(time[0] =='0'){
                first = stoi(time.substr(1 , 1));
            }else{
                first = stoi(time.substr(0,2));
            }
            if(time[3] == '0') {
                offset = stoi(time.substr(4 , 1));
            }else{
                offset = stoi(time.substr(3,2));
            }

            return (60*first)+(offset);
        };

        for(int i = 0; i < timePoints.size(); ++i) {
            int num = convert(timePoints[i]);
            // cout<<num<<" "<<timePoints[i]<<endl;
            if(timeline[num]) {
                return 0;
            }
            timeline[num] = 1;
        }

        int prev = -1;
        int mini = 1440;
        int first = -1;
        for(int i = 0; i < 1440; ++i) {
            if(timeline[i]){
                if(prev == -1){
                    prev = i;
                    first = i;
                    continue;
                }
                mini = min(mini , i - prev);
                prev = i;
            }
        }

        return min(mini , 1440 - prev + first);
    }
};