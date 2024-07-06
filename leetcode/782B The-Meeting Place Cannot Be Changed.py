def solve():
    n = int(input())
    dis = list(map(int , input().split()))
    speed = list(map(int , input().split()))

    def magic(point):
        t = float('-inf')
        for i in range(n):
            t = max(t , abs(point - dis[i])/speed[i])
        
        return t

    
    l = min(dis)
    r = max(dis)

    ite = 100

    while ite:
        mid1 = l + (r -l)/3
        mid2 = r - (r-l)/3

        val1 = magic(mid1)
        val2 = magic(mid2)

        if val1 == val2:
            l = mid1
            r = mid2
        elif val1 > val2:
            l = mid1
        else:
            r = mid2
        ite -= 1
    

    print(magic(mid1))
       

# n = int(input())
n = 1
for _ in range(n):
    solve()