# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        array = list(s)
        hash = {}
        for i in s:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        print(hash)        
        for key, value in hash.items():
            print(key)
            print(value) 
            if value == 1:
                return array.index(key)
        return -1
            
            