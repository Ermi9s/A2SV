class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def converter(bit):
            if bit == 1:
                return 0
            else:
                return 1

        ans = [[] for _ in range(len(image))]

        for i in range(len(image)):
            while image[i]:
                ans[i].append(converter(image[i].pop()))
        
        return ans


        