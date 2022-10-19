class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        length = len(needle)
        for index in range(len(haystack) - length + 1):
            if haystack[index:index+length] == needle:
                return index
        
        return -1