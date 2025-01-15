class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
          
class Trie:
    def __init__(self):
        self.root = TrieNode()
 
    def add(self,num):
        current = self.root

        for i in range(32 , -1 , -1):
            val = int(((1 << i) & num) != 0)
            if val == 1:
                if not current.one:
                    current.one = TrieNode()
                current = current.one
            else:
                if not current.zero:
                    current.zero = TrieNode()
                current = current.zero

    
    def search(self,num):
        current = self.root
        res = 0
        for i in range(32 , -1 , -1):
            val = int(((1 << i) & num) != 0)
            want = 1 - val
            
            if val == 1:
                if current.zero:
                    current = current.zero
                elif current.one:
                    res |= (1 << i)
                    current = current.one
            else:
                if current.one:
                    res |= (1 << i)
                    current = current.one
                elif current.zero:
                    current = current.zero

        return res
                
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = []
        mini = min(nums)
        for num in nums:
            heappush(heap , num)
        
        ans = [0] * len(queries)
        for i in range(len(queries)):
            queries[i].append(i)
        
        queries.sort(key = lambda x : x[1])

        trie = Trie()

        for x,m,i in queries:
            while heap and heap[0] <= m:
                num = heappop(heap)
                trie.add(num)
         
            if m < mini:
                ans[i] = -1
                continue

            res = trie.search(x)
            ans[i] = res^x

        return ans        

        


        