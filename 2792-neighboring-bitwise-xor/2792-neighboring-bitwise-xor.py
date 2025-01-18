class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = [0]

        for i in range(len(derived)-1):
            val = ans[-1] ^ derived[i]
            ans.append(val)
        
        if ans[0] ^ ans[-1] == derived[-1]:
            return True

        ans = [1]

        for i in range(len(derived)-1):
            val = ans[-1] ^ derived[i]
            ans.append(val)

        if ans[0] ^ ans[-1] == derived[-1]:
            return True
        

        return False
        
