class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();

        if(m == 0){
            if(n%2){
                return nums1[n/2];
            }else{
                return (double)(nums1[(n/2) - 1] + nums1[n/2])/2;
            }
        }

        if(n == 0){
            if(m%2){
                return nums2[m/2];
            }else{
                return (double)(nums2[(m/2) - 1] + nums2[m/2])/2;
            }
        }



        int l = -2;
        int r = n;
        int half = (m+n)/2;

        while(l+1 < r) {
            int mid = l + (r-l)/2;

            int left1 = mid;
            int left2 = half - (mid+1) - 1;

            if(left2 >= m){
                l = mid;
                continue;
            }
            if(left1+1 > half){
                r = mid;
                continue;
            }

            int num_l1 = ((left1 != -1)? nums1[left1] : -2e6);
            int num_l2 = ((left2 != -1)? nums2[left2] : -2e6);

            int num_r1 = ((left1 != n-1)? nums1[left1 + 1] : 2e6);
            int num_r2 = ((left2 != m-1)? nums2[left2 + 1] : 2e6);

            if(num_l1 <= num_r2 && num_l2 <= num_r1){
                double mx_l = max(num_l1 , num_l2);
                double mn_r = min(num_r1 , num_r2);

                if((m+n)%2){
                    return mn_r;
                }else{
                    return (mn_r + mx_l)/2;
                }

            }else if(num_l1 <= num_r2){
                l = mid;
            }else{
                r = mid;
            }

        }


        l = -2;
        r = m;
        while(l+1 < r) {
            int mid = l + (r-l)/2;

            int left1 = mid;
            int left2 = half - (mid+1) - 1;

            if(left2 >= n){
                l = mid;
                continue;
            }

            if(left1+1 > half){
                r = mid;
                continue;
            }

            int num_l1 = ((left1 != -1)? nums2[left1] : -2e6);
            int num_l2 = ((left2 != -1)? nums1[left2] : -2e6);

            int num_r1 = ((left1 != m-1)? nums2[left1 + 1] : 2e6);
            int num_r2 = ((left2 != n-1)? nums1[left2 + 1] : 2e6);

            if(num_l1 <= num_r2 && num_l2 <= num_r1){
                double mx_l = max(num_l1 , num_l2);
                double mn_r = min(num_r1 , num_r2);

                if((m+n)%2){
                    return mn_r;
                }else{
                    return (mn_r + mx_l)/2;
                }

            }else if(num_l1 <= num_r2){
                l = mid;
            }else{
                r = mid;
            }

        }
        return 0;
    }
};