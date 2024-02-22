class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        pos = k
        while tickets[pos] != 0:
            print(pos)
            tickets[0] -= 1
            if tickets[0] > 0:
                temp = tickets.pop(0)
                tickets.append(temp)
    
                if pos != 0:
                    pos -= 1
                else:
                    pos = len(tickets) - 1
            elif tickets[0] == 0 and pos != 0:
                tickets.pop(0)
                if pos != 0:
                    pos -= 1
                else:
                    pos = len(tickets) - 1
                
            time += 1

        return time
            
            


        