class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        ref = sorted([(intervals[i][0] , i) for i in range(len(intervals))])
        print(ref)
        def search(num):
            l = -1
            r = len(ref)-1

            while l+1 < r:
                mid = (l+r)//2

                if ref[mid][0] < num:
                    l = mid
                else:
                    r = mid
            
            return -1 if ref[r][0] < num else ref[r][1]
        

        for pair in intervals:
            ans.append(search(pair[1]))
        
        return ans


        


        