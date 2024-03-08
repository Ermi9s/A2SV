from bisect import bisect_right
def solve():
    n = int(input())
    nums = list(map(int , input().split()))
    m = int(input())
    nums.sort()
    for _ in range(m):
        pric = int(input())
        print(bisect_right(nums , pric))
    
    
    
# n = int(input())
n = 1
for _ in range(n):
    solve()