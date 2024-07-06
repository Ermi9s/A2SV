class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        W = 0

        for i in blocks[:k]:
            if i == "W":
                W += 1
        ans = W

        for l in range(len(blocks) - k):
            if blocks[l] == "W":
                W -= 1
            if blocks[l+k] == "W":
                W += 1
            ans = min(W,ans)
        
        return ans


        