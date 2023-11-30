class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = 0
        temp = {}

        for i in nums:
            temp[i] = temp.get(i,0) + 1 #{1:3,2:1,3:2}
        
        print(temp)
        
        for n in temp.values():
            pair += (n*(n-1))//2
        

        return pair
        