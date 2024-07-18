class Solution:
    def longestDecomposition(self, text: str) -> int:
        text = text.strip()
        count = 0 
        if len(text) == 1:
            count += 1
        for i in range(len(text)//2):
            if text[:i+1] == text[len(text)-1-i:]:
                count += 2
                if len(text) >= 2:
                    count += self.longestDecomposition(text[i+1:len(text)-i-1])
                    break
                else:
                    count += 1
            if (i+1)*2 >= len(text) -1:
                count += 1
        return count


