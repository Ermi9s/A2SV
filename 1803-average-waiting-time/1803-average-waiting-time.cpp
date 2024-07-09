class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        long time = customers[0][0];
        double waiting = 0;

        for(auto customer : customers){
            if(time < customer[0]){
                time = customer[0] + customer[1];
            }else{
                time += customer[1];
            }

            waiting += (time - customer[0]);
        }

        
        return waiting/customers.size();
    }
};