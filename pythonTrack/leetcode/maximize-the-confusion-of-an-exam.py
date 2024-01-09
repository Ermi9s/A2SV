class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        d = dict()
        d['T'] = 0
        d['F'] = 0
        l = 0
        count = 0

        for r,n in enumerate(answerKey):
            d[n] += 1
            while ((d['T'] > k and d['F'] > k)) and l < r:
                d[answerKey[l]] -= 1
                l += 1
            count = max((r-l+1),count)
        
        return count

        