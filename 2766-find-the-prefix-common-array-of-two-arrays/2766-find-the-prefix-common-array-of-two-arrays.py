class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = [len(A)]
        count = { i : 2 for i in range(len(A)+1)}

        for i in range(len(A)-1,0,-1):
            if A[i] == B[i]:
                count[A[i]] -= 2
                ans.append(ans[-1] - 1)
            else:
                count[A[i]] -= 1
                count[B[i]] -= 1
                ans.append(ans[-1] - (count[A[i]] + count[B[i]]))
        
     
        return ans[::-1]
