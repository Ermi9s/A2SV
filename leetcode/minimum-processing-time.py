class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        count = []
        for i in range(0,len(tasks),len(tasks)//len(processorTime)):
            count.append(tasks[i])
        
        res = 0
        print(count)
        for i in range(len(count)):
            res = max(res , count[i] + processorTime[i])
        
        return res