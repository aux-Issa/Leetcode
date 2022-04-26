# https://leetcode.com/problems/top-k-frequent-elements/
# 解説: https://www.youtube.com/watch?v=YPTqKIgVk-k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # 0〜numsの長さを格納する配列を作る=同じ数字の登場回数は0-lenであるため
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            # 各数字の登場回数を格納していく
            # hashであるcountのkeyは数字，valは登場回数となる
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            # freqの要素は配列なのでappendする
            # freqのindexが登場回数，要素が数字(array)
            freq[c].append(n)
        res = []
        # 登場回数の多い順(descending order)にresに格納していく
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                