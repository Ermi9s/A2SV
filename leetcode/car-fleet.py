class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ch = [[p , s] for p , s in zip(position , speed)]

        ch.sort()

        time = [(target - po)/v for po,v in ch]
        time = time[::-1]
        stk = [time[0]]

        for i in range(1 , len(time)):
            if time[i] > stk[-1]:
                stk.append(time[i])
        

        
        return len(stk)
        