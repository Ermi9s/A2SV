class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stk = ["/"]
    
        for i in paths:
            if i == "" or i == ".":
                continue
            
            if i == ".." and len(stk) != 1:
                stk.pop()
                stk.pop()
            elif i != "..":
                stk.append(i)
                stk.append("/")
        
        if len(stk) > 1 and stk[-1] == "/":
            stk.pop()
        
        return ''.join(stk)

        