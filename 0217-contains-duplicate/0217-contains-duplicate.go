func containsDuplicate(nums []int) bool {
    ch := make(map[int]int , len(nums));
    var flag bool;
    for i := range(len(nums)) {
        if ch[nums[i]] > 0 {
            flag = true;
            break
        }
        ch[nums[i]]++;
    }

    return flag;
}