class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def check(base , temp):
            res = 0
            for i in temp.keys():
                res += (base[i] - temp[i])
            return res == 0


        base = Counter(s)
        temp = defaultdict(int)
        ans = []
        l = 0
        for i in range(len(s)):
            temp[s[i]] += 1

            if check(base , temp):
                ans.append(i-l + 1)
                l = i + 1
        
        return ans
            



        