class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        pattern = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                pattern[i+j].append(mat[i][j])
        ans = []
        for k in pattern.keys():
            if k % 2 == 0:
                while pattern[k]:
                    ans.append(pattern[k].pop()) 
            else:
                for v in pattern[k]:
                    ans.append(v)
        
        return ans

        