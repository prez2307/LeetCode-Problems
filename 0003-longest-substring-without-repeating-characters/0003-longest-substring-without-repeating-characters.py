class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        length = len(s)
        left = 0
        right = 0
        res = 0
        while right < length:
            if s[right] not in seen:
                res = max(res, right - left + 1)
            else:
                if seen[s[right]] < left:
                    res = max(res, right - left + 1)
                else:
                    left = seen[s[right]] + 1
            seen[s[right]] = right
            right += 1
        return res