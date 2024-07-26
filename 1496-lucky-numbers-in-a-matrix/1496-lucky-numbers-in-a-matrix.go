func luckyNumbers (matrix [][]int) []int {
    row_ch := make(map[int]int)
    col_ch := make(map[int]int)
    
    for i := range len(matrix) {
        row_ch[i] = min(matrix[i]);
    }

    for j := 0; j < len(matrix[0]); j++ {
        maxi := 0
        for i := 0; i < len(matrix); i++ {
            if matrix[i][j] > maxi {
                maxi = matrix[i][j];
            }
        }
        col_ch[j] = maxi;
    }

    ans := make([]int , 0);
    for i := range len(matrix) {
        for j := range len(matrix[0]) {
            if col_ch[j] == matrix[i][j] && row_ch[i]== matrix[i][j] {
                ans = append(ans , matrix[i][j])
            }
        }
    }
    return ans;
    
}

func min(arr []int) int{
    mini := 1000000;
    for i := range len(arr) {
        if arr[i] < mini {
            mini = arr[i];
        }
    }
    return mini;
}