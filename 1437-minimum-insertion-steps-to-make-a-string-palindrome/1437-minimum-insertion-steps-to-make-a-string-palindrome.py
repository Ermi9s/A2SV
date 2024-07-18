class Solution:
    def minInsertions(self, s: str) -> int:
        r=s[-1::-1]
        p=[0]*(len(s)+1)
        
        
        for i in range(1,len(s)+1):
            c=[0]*(len(s)+1)
            for j in range(1,len(s)+1):
                if s[i-1]==r[j-1]:
                    c[j]=1+p[j-1]
                else:
                    c[j]=max(p[j],c[j-1])
            p=c
        return len(s)-c[-1]