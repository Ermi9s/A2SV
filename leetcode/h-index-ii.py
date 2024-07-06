class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = -1
        r = max(citations)+1

        while l + 1 < r:
            mid = (l+r)//2
            key = bisect_left(citations , mid)
      
            if mid <= (len(citations) - key):
                l = mid 
            else:
                r = mid 
        
        return l
        
        

        
        
        