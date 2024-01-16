class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        w = len(cardPoints) - k
        t = sum(cardPoints)

        pre = sum(cardPoints[:w])
        
        ans = t - pre
        if w == 0:
            return ans
        for l in range(1 , len(cardPoints) - w + 1):
            pre -= cardPoints[l-1]
            pre += cardPoints[l+w -1]
        
            ans = max(ans , t - pre)
        
        return ans


        
        