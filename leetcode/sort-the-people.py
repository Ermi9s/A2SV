class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
       
        for i , j in zip(names, heights):
            d[j] = i
        
        heights.sort(reverse = True)

        ans = []

        for i in heights:
            ans.append(d[i])

        return ans
        
        

            
        