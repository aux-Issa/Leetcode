# https://leetcode.com/problems/group-anagrams/
# solution: https://p0ny.hatenablog.com/entry/2020/03/15/213608

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        for word in strs:
            sorted_chars = "".join(sorted(word))
            if sorted_chars in dic:
                dic[sorted_chars].append(word)
            else:
                dic[sorted_chars] = [word]
        # for s in dic:
        #     ans.append(dic[s])
        # return ans
        return [dic[s] for s in dic]
            
