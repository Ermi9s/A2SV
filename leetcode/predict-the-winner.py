class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(left, right):
            if left == right:
                return nums[left]
            left_choice = nums[left] - play(left+1, right)
            right_choice = nums[right] - play(left, right-1)

            return max(left_choice, right_choice)


        return play(0, len(nums) - 1) >= 0
        

            

            
