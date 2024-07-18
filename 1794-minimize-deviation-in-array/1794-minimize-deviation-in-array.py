import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = list(set(nums))
        heap = []
        max_heap = 0
        
        for num in nums:
            if num%2 == 0:
                max_heapvalue = num
            else:
                max_heapvalue = 2*num

            while num%2 == 0:
                num //= 2
            max_heap = max(max_heap, num)
            heapq.heappush(heap, (num, max_heapvalue))
            
        res = inf
        while heap:
            num, max_heapvalue = heapq.heappop(heap)
            res = min(res, max_heap - num)
            
            if num == max_heapvalue:
                return res
            
            heapq.heappush(heap, (2*num, max_heapvalue))
            if 2*num > max_heap:
                max_heap = 2*num
        
        return res