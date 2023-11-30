class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = []
        for i in range(len(command)):
            if command[i] == "G":
                ans.append("G")
            if command[i] == "(" and command[i+1] == ")":
                ans.append("o")
            if command[i] == "(" and command[i+1] == "a":
                ans.append("al")
        
        return "".join(ans)



        