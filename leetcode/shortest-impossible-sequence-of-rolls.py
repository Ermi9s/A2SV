class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # mi = 0
        ch = set()
        nw = 1
        for i in range(len(rolls)):
            ch.add(rolls[i])
            if len(ch) == k:
                # mi = i
                nw += 1
                ch.clear()
        
        return nw
        



        