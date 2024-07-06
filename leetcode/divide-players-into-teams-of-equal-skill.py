class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        l = 0
        r = len(skill) - 1
        test = set()
        chemo = 0
        while l < r:
            test.add(skill[l] + skill[r])
            chemo += skill[l] * skill[r]
            l += 1
            r -= 1

       
       
        if len(test) != 1:
            return -1
        else:
            return chemo

        