# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set_ans = set1.intersection(nums2)
        list_ans = list(set_ans)
        return list_ans


        # 別解
        # ans = []
        # for num in nums1:
        #     if num in nums2 and num not in ans:
        #         ans.append(num)
        # return ans