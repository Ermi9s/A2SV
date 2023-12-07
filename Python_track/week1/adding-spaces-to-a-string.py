class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        answer = []

        start = 0
        for end in spaces:
            answer.append(s[start:end])
            start = end
        answer.append(s[spaces[-1]:])
        
        return ' '.join(answer)
        