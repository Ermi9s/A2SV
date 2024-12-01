class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        mp = set()

        for i in range(len(arr)):
            if arr[i]/2 in mp:
                return True
            mp.add(arr[i])
    
        mp = set()

        for i in range(len(arr)-1 , -1 , -1):
            if arr[i]/2 in mp:
                return True
            mp.add(arr[i])
        
        return False
        