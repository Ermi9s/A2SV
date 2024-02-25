class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pen = [0]*(len(customers)+1)

        y = customers.count('Y')
        n = 0

        pen[0] = y

        for i in range(len((customers))):
            if customers[i] == 'Y':
                y -= 1
            else:
                n += 1
            
            pen[i+1] = y + n

        ind = 0

        for i in range(len(pen)):
            if pen[i] < pen[ind]:
                ind = i

        return ind 
                
        