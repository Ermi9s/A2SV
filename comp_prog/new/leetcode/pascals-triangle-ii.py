class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        lst = self.getRow(rowIndex - 1)
        nwlst = [1]

        l = 0
        r = 1

        while r < len(lst):
            nwlst.append(lst[l] + lst[r])
            l += 1
            r += 1
        nwlst.append(1)
        
        return nwlst

            