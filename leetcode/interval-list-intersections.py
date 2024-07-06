class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def intersected(arr1 , arr2):
            return arr1[1] >= arr2[0]

        def compa(arr1 , arr2):
            temp = []
            if arr1[0] >= arr2[0]:
                temp.append(arr1[0])
            else:
                temp.append(arr2[0])

            if arr1[1] <= arr2[1]:
                temp.append(arr1[1])
            else:
                temp.append(arr2[1])

            return temp

        def mashUp(obj1 , obj2):
            big = []
            for i in obj1:
                big.append(i)

            for i in obj2:
                big.append(i)
            
            big.sort()

            return big

        myLst = mashUp(firstList , secondList)
        ans = []
        l = 0
        r = 1
        while r < len(myLst):
            if l == r:
                r += 1
                continue

            if intersected(myLst[l] , myLst[r]):
                ans.append(compa(myLst[l] , myLst[r]))
                r += 1
                continue
            l += 1
            
        
        return ans


