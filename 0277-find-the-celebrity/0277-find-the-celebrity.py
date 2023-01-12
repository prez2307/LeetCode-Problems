# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0

        for right in range(n):
            if knows(celebrity, right) == 0:
                continue

            if knows(celebrity, right) == 1:
                celebrity = right
        
        for i in range(n):
            if i != celebrity:
                if knows(i, celebrity) and not knows(celebrity, i):
                    continue
                else:
                    return -1

        
        return celebrity
