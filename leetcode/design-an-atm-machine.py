class ATM(object):
    def __init__(self):
        self.depo = [0]*5
           
    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i,note in enumerate(banknotesCount):
            self.depo[i] += note

        
    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        reference = [20,50,100,200,500]
        answer = [0]*5

        for i in range(4,-1,-1):
            temp = amount//reference[i]
            answer[i] =  min(temp , self.depo[i])
            amount -= answer[i] * reference[i]
            self.depo[i] -= answer[i]
        
        if amount == 0:
            return answer
        
        self.deposit(answer)
        return [-1]

    
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)