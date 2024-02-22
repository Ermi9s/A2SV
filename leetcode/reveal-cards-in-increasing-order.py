class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) == 1:
            return deck
            
        res = deque()

        deck.sort(reverse = True)

        res.appendleft(deck[0])
        for i in range(1, len(deck)):
            temp = res.pop()
            res.appendleft(temp)
            res.appendleft(deck[i])
        
        return res
        



        