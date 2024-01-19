class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0 
        r = 0
        count = defaultdict(int)
        mini = float('inf')
        while(r < len(cards)):
            count[cards[r]] += 1

            while count[cards[r]] > 1:
                mini = min(mini , r-l+1)
                count[cards[l]] -= 1
                l += 1
            
            r += 1
        
        return mini if mini != float('inf') else -1

        