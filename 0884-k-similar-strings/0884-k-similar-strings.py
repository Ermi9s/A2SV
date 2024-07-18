class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbours(s):
            i = 0
            while s[i] == s2[i]:
                i += 1
            for j in range(i+1, len(s)):
                if s[j] == s2[i]:
                    yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        q = collections.deque([(s1, 0)])
        seen = {s1}
        while q:
            s, d = q.popleft()
            if s == s2:
                return d
            for nei in neighbours(s):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, d+1))
        return -1