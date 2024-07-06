from bisect import bisect_right
def solve():
    n = int(input())
    nums = list(map(int , input().split()))
    m = int(input())
    price = []
    nums.sort()
    for _ in range(m):
        price = int(input())
        print(bisect_right(nums , price))
    
    
    
# n = int(input())
n = 1
for _ in range(n):
    solve()