class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fun(n):
            if n == 1:
                return ["1"]
            result = []
            for item in fun(n-1):
                for index in range(len(item)+1):
                    new_item = item[:index] + str(n) + item[index:]
                    result.append(new_item)
            return result
        result = fun(n)
        result.sort()
        return result[k-1]       