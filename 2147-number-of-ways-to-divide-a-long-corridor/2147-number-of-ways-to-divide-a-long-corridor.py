class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = 0
        seats = []
        for i in range(len(corridor)):
            char = corridor[i]
            if char is 'S':
                count += 1
                seats.append(i)
        if count % 2 == 1 or count < 2:
            return 0
        
        ans = 1
        for i in range(len(seats) // 2 - 1):
            ans *= seats[2*i+2] - seats[2*i+1]
        
        return ans % (10**9 + 7)