class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ch = defaultdict(int)

        l = 0
        r = 0
        picked = 0
        while r < len(fruits):
            ch[fruits[r]] += 1
            
            while len(ch) > 2:
                ch[fruits[l]] -= 1

                if ch[fruits[l]] == 0:
                    del(ch[fruits[l]])

                l += 1
                
            picked = max(picked , r - l + 1)
            r += 1
        
        return picked 