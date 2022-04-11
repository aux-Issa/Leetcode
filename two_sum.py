# https://leetcode.com/problems/two-sum/
# Solution: https://www.youtube.com/watch?v=KLlXCFG5TnA
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[value] = i
        return False
          