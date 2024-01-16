class Solution:
    def minWindow(self, s: str, t: str) -> str:
        base = defaultdict(int)
        temp = defaultdict(int)
        n = len(s)

        if n < len(t):
            return ""

        for i in t:
            base[i] += 1
        
        l = 0
        r = 0
        win = n + 1
        flag = 0
        ans = []

        while r < n:
            if s[r] in base:
                temp[s[r]] += 1
                if temp[s[r]] == base[s[r]]:
                    flag += 1
            
            while l <= r and flag == len(base):

                if r - l + 1 < win:
                    ans = s[l:r+1]
                    win = r-l+1

                if s[l] in temp:
                    temp[s[l]] -= 1
                    if temp[s[l]] < base[s[l]]:
                        flag -= 1
                
                l +=1

            r += 1


        return ''.join(ans) if ans else ""



        
