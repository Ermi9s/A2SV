from collections import defaultdict
def solve():
    n= int(input())
    nums = input()
    
    ans = 0

    ch = defaultdict(int)
    ch[1] = 1
    
    sums = 0 
    for i in range(len(nums)):
        sums += int(nums[i])
        ans += ch[sums - i]
        ch[sums - i] += 1
    
    print(ans)
    

n = int(input())
# n = 1
for _ in range(n):
    solve()