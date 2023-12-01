class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        mp = {}
        for i in range(len(order)):
            mp[order[i]] = i
        

        for w in  range(len(words)-1):
            bef = words[w]
            aft = words[w+1]

            for i in range(min(len(bef),len(aft))):
                if mp[bef[i]] > mp[aft[i]]:
                    return False
                elif mp[bef[i]] < mp[aft[i]]:
                    break
            
            else:
                if len(bef) > len(aft):
                    return False
                
        return True
            
           
            

            

        


        # 0,


        
        