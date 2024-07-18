class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        frequency = {}
        words_count = len(words)
        words_length = len(words[0])
        res = []

        for c in words:
            frequency[c] = frequency.get(c, 0) + 1

        for i in range(len(s) - (words_count * words_length) + 1):
            words_seen = {}
            for j in range(words_count):
                next_word_index = i + j * words_length
                next_word = s[next_word_index: next_word_index + words_length]
                if next_word not in frequency:
                    break
                words_seen[next_word] = words_seen.get(next_word, 0) + 1
                if words_seen[next_word] > frequency[next_word]:
                    break
                if j + 1 == words_count:
                    res.append(i)

        return res