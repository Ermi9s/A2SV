class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+1)

        for left,right,seats in bookings:
            prefix[left-1] += seats
            prefix[right] -= seats
        
        for i in range(1 , n+1):
            prefix[i] += prefix[i-1]
        prefix.pop()

        return prefix


        
        