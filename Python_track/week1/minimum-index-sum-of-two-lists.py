class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        counter = {}
        min_ind = float('inf')
        result = []

        #mark up the indices of the first list
        for ind,string in enumerate(list1):
            if string in list2:
                counter[string] = ind
        
        
        for ind,string in enumerate(list2):
            counter[string] = counter.get(string, (-ind-1)) + ind
        
        #now find the the min index sum not equal to zero
        for inds in counter.values():
            if inds >= 0:
                min_ind = min(inds,min_ind)
        
        #finaly append the keys with min_ind to result
        for key in counter.keys():
            if counter[key] == min_ind:
                result.append(key)
        
        return result
        

        

        