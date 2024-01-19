class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        for i in matrix:
            for j in range(1 , len(i)):
                i[j] += i[j-1]
        
        ans = 0

        for bound in range(len(matrix[0])):
            for c in range(bound , len(matrix[0])):
                count = defaultdict(int)
                count[0] = 1
                run = 0

                for r in range(len(matrix)):
                    run += matrix[r][c] - (matrix[r][bound-1] if bound > 0 else 0)
                    
                    if run - target in count.keys():
                        ans += count[run - target]

                    count[run] += 1
        

        return ans

                

                
                
        