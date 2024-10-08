class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>>dp(text1.size()+1 , vector<int>(text2.size()+1 , 0));

        for(int i = 0; i < text1.size()+1; ++i) {
            for(int j = 0; j < text2.size()+1; ++j){
                if( !i || !j) dp[i][j] = 0;
                else{
                    if(text1[i-1] == text2[j-1]) {
                        dp[i][j] = dp[i-1][j-1]+1;
                    }
                    dp[i][j] = max(dp[i][j] , dp[i-1][j]);
                    dp[i][j] = max(dp[i][j] , dp[i][j-1]);
                }
            }
        }

        return dp[text1.size()][text2.size()];

    }
};