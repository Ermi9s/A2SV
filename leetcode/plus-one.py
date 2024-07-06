class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = [1]
        carry = 0
        one = 1

        for i in range(len(digits)-1, -1 , -1):
            digits[i] = digits[i] + one + carry

            if digits[i] < 10:
                carry = 0
                return digits
            elif digits[i] >= 10:
                digits[i] = 0
                carry = 1
            
            one = 0

        if carry:
            ans.extend(digits)
        
        return ans
            

            
        