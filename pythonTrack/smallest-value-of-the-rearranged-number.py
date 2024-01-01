class Solution:
    def smallestNumber(self, num: int) -> int:
        snum = str(num)
        lst = [i for i in snum if i != '-']
        if num < 0:
            lst.sort(reverse = True)
            ans = ''.join(lst)
            return 0 - int(ans)
        else:
            lst.sort()

            if lst[0] == '0':
                for i in range(len(lst)):
                    if lst[i] != '0':
                        lst[0],lst[i] = lst[i],lst[0]
                        break

            ans = ''.join(lst)  

            return int(ans)
            


        
        