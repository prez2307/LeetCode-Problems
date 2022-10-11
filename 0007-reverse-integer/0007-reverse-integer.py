class Solution:
    def reverse(self, x: int) -> int:
        strVers = str(x)
        final = ''
        neg = False
        for i in reversed(range(len(strVers))):
            if strVers[i] == '-':
                neg = True
            final += strVers[i]
        
        if neg:
            final = final[:len(final)-1]
            ans = -1 * int(final)
            if ans < -2**31:
                return 0
            else:
                return ans
        return int(final) if int(final) < 2**31 - 1 else 0