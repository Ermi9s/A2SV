class Solution {
  List<int> twoSum(List<int> nums, int target) {
    var ch = Map();
    var ans = [-1 , -1];
    for(int i = 0; i < nums.length; i++){
        if(ch.containsKey(target - nums[i])) {
            ans[0] = i;
            ans[1] = ch[target - nums[i]];
            break;
        }

        ch[nums[i]] = i;
    }

    return ans;
  }
}