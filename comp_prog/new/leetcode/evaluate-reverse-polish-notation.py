class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {'*','/','+','-'}

        for i in tokens:
            stk.append(i)
          
            if stk[-1] in ops:
                operation = stk.pop()
                b = int(stk.pop())
                a = int(stk.pop())

                if operation == "+":
                    res = (a + b)
                    
                elif operation == "-":
                    res = (a - b)
                    
                elif operation == "*":
                    res = (a * b)
                    
                elif operation == "/":
                    res = (a / b)
                
                stk.append(res)
                   
        
       
        return int(stk[-1] )
