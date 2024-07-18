class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        M, N = len(words[0]), len(target)
        counts = defaultdict(Counter)
        for word in words:
            for j in range(M):
                counts[j][word[j]] += 1

        @cache
        def dfs(i, j):
            if i >= N: return 1
            if j >= M: return 0
            cnt = dfs(i, j + 1)
            if counts[j][target[i]] > 0:
                cnt += (dfs(i + 1, j + 1) * counts[j][target[i]]) % MOD
            return cnt % MOD

        return dfs(0, 0)