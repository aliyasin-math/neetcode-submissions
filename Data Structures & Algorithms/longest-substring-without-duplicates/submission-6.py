class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_Set = set()
        
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in char_Set:
                char_Set.remove(s[l])
                l += 1
            char_Set.add(s[r])
            res = max(res, r-l+1)
        return res