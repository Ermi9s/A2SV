class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []

        for i in arr2:
            for ind, j in enumerate(arr1):
                if j == i:
                    ans.append(j)
                    arr1[ind] = -1

        arr1.sort()           
        for i in arr1:
            if i != -1:
                ans.append(i)

        
        return ans
        