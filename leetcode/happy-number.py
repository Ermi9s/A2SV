class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def break_up(number):
            lst = []
            while number:
                lst.append(number%10)
                number //= 10
            return lst

        loop = set()
       

        num = break_up(n)
        prod = 0

        while True:
            prod = 0
            for i in num:
                prod += pow(int(i),2)
                
            num = break_up(prod)
           
            if prod == 1:
                return True

            if prod in loop:
                return False
            
            loop.add(prod)
            
            

            


        


        