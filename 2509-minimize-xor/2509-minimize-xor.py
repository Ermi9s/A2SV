class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = 0
        x = 0

        for i in range(32):
            if (1 << i) & num2:
                count += 1
        c = 33
        while count and c >= 0:
            if (1 << c) & num1:
                x |= (1 << c)
                count -= 1
            c -= 1
        c = 0

        while count:
            if not ((1 << c) & num1):
                x |= (1 << c)
                count -= 1
            c += 1

        return x 