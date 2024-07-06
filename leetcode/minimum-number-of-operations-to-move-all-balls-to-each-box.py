class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        position  = {}
        moves = []

        for ind,one in enumerate(boxes):
            if one == "1":
                position[str(ind)] = ind
        
        
        for ind,num in enumerate(boxes):
            if num == 0:
                move = 0
                for pos in position.values():
                    move += abs(ind - pos)
                moves.append(move)
            else:
                move = 0
                for pos in position.values():
                    if pos != ind:
                        move += abs(ind - pos)
                moves.append(move)  

        return moves         



            

        
