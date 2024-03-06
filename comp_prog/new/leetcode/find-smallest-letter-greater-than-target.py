class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = -1
        r = len(letters)-1

        while l+1 < r:
            mid = (l+r)//2

            if letters[mid] > target:
                r = mid
            else:
                l = mid
        

        return letters[r] if letters[r] > target else letters[0]
        
            
        