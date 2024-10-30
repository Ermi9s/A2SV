class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0]*(4 * self.n)
        self.arr = nums[:]
        self.build(0 , 0 , self.n - 1)
    
    def getChildren(self , root):
        left = 2*root + 1
        right = 2*root + 2
        return left,right

    def build(self, node , nLeft , nRight):
        if nLeft == nRight:
            self.tree[node] = self.arr[nLeft]
            return
        
        left,right = self.getChildren(node)
        mid = (nLeft + nRight)//2

        self.build(left , nLeft , mid)
        self.build(right , mid+1 , nRight)

        self.tree[node] = self.tree[left] + self.tree[right]
    
    def update(self , node , nLeft , nRight , index,  val):
        if nLeft == nRight:
            self.arr[index] = self.tree[node] = val
            return
        
        left,right = self.getChildren(node)
        mid = (nLeft + nRight)//2

        if index <= mid:
            self.update(left , nLeft , mid , index , val)
        else:
            self.update(right , mid+1 , nRight , index , val)

        self.tree[node] = self.tree[left] + self.tree[right]

    def getSum(self , node , nLeft , nRight , qLeft ,qRight):
        if qLeft > qRight:
            return 0
        if qLeft == nLeft and qRight == nRight:
            return self.tree[node]

        left,right = self.getChildren(node)
        mid = (nLeft + nRight)//2

        leftSum = self.getSum(left , nLeft , mid , qLeft, min(mid , qRight))
        rightSum = self.getSum(right , mid+1 , nRight , max(mid+1 , qLeft), qRight)

        return leftSum + rightSum 

    def easyUpdate(self , index , val):
        self.update(0 , 0 , self.n-1, index , val)

    def easyGet(self , ql , qr):
        return self.getSum(0 , 0 , self.n-1 , ql,  qr)

        
class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = SegTree(nums)
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.easyUpdate(index , val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.easyGet(left , right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)