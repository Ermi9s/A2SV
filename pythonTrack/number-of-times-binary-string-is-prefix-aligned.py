class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        sums = 0
        nth = 0
        count = 0

        for n in flips:
            sums += n
            nth =  max(nth , n)
            s = int((nth/2)*(1+nth))
            if sums == s:
                count += 1
        
        return count








        