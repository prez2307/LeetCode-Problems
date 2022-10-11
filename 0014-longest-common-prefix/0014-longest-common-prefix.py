class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = strs[0]
        for s in strs[1:]:
            curr = ''
            for i in range(min(len(s), len(temp))):
                if s[i] != temp[i]:
                    break
                else:
                    curr += s[i]
            temp = curr
        
        return temp