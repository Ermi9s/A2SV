class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-nums[i] for i in range(len(nums))]
        heap.sort()

        score = 0
        while heap and k:
            num = heappop(heap)
            num *= -1
            score += num
            heappush(heap , -((num + 2)//3))
            k -= 1
        
        return score
