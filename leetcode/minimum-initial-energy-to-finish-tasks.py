class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0] , reverse = True)

        base = 0
        spent = 0
        curr = 0
        for i in tasks:
            if curr < i[1]:
                base += (i[1] - curr)
        
            spent += i[0]
            curr = base - spent
        
        return base

        