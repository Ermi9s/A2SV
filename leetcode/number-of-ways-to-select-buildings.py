class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = {1 : 0 , 2 : 0 , 3 : 0}
        one = {1 : 0 , 2 : 0 , 3: 0}

        for i in s:
            if i == "0":
                zero[1] += 1
                zero[2] += one[1]
                zero[3] += one[2]
            else:
                one[1] += 1
                one[2] += zero[1]
                one[3] += zero[2]
        
        return zero[3] + one[3]


        