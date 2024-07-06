class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        answers.sort()

        streak = answers[0]
        ans += (answers[0]+1)
        prev = answers[0]
        for i in range(1 , len(answers)):
            if streak and answers[i] == prev > 0:
                streak -= 1
                continue

            ans += (answers[i] + 1)
            streak = answers[i]
            prev = answers[i]
        
        return ans
                

    

        