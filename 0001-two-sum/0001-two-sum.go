func twoSum(nums []int, target int) []int {
   mp := make(map[int]int)
    ans := []int{0 , 0};

    for i := range len(nums) {
        if val,ok := mp[target - nums[i]]; ok {
            ans[0] = i;
            ans[1] = val;
            break;
        }
        mp[nums[i]] = i;
    }

    return ans;
}