class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        maxi = sum(nums)+1
        mini = 0
        ans = []

        def count(mini , maxi):
            if mini + 1 >= maxi:
                return 

            mid = (maxi + mini)//2

            ship = 1
            sums = 0

            for i in range(len(nums)):
                if sums > mid:
                    ship += (days + 1)
                # print(ship)
                sums += nums[i]
                if sums > mid:
                    ship += 1
                    sums = nums[i]
            if sums > mid:
                ship += (days + 1)
    

            if ship <= days:
                # print(mid)
                ans.append(mid)
                count(mini , mid)
            else:
                count(mid , maxi)
        
        count(mini , maxi)

        return min(ans)



        