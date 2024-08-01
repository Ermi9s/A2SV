func countSeniors(details []string) int {
    ans := 0
    for _,info := range details {
        if info[11] >= '6' {
            if info[11] == '6' && info[12]=='0'{
                continue
            }
            ans += 1
        }
    }
    return ans
}