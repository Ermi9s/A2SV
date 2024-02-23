class Solution:
    def lemonadeChange(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for i in nums:
            if i == 5:
                count[i] += 1
            elif i == 10:
                if count[5] > 0:
                    count[5] -= 1
                else:
                    return False
                count[i] += 1
            else:
                if count[5] > 0 and count[10] > 0:
                    count[5] -= 1
                    count[10] -= 1
                elif count[5] > 2:
                    count[5] -= 3
                else:
                    return False
                count[i] += 1

        return True
