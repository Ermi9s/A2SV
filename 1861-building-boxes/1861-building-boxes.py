class Solution:
    def minimumBoxes(self, n: int) -> int:
        answer=curr=i=j=0
 
        while curr<n:  
            if j<i:
                j+=1
            else:
                j=1
                i+=1                
            curr+=j
            answer+=1

        return answer

            


    