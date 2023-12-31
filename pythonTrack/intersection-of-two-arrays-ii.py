class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dnum = defaultdict(int)

        for i in nums1:
            dnum[i] += 1
        
        ans = []
        for i in nums2:
            if dnum[i] > 0:
                ans.append(i)
                dnum[i] -= 1
        
        return ans



        