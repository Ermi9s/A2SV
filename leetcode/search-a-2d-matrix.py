class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        def rowSearch(num):
            l = 0
            r = len(matrix)

            while l+1 < r:
                mid = (l+r)//2
                
                if matrix[mid][0] <= num:
                    l = mid
                else:
                    r = mid
            
            return l


        row = rowSearch(target)
        l = 0
        r = len(matrix[0])-1

        while l <= r:
            mid = (l+r)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False 
        