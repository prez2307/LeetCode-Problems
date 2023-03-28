class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        prefix_sum = [0]
        positions = []
        num_fruits = []
        for pos, count in fruits:
            prefix_sum.append(prefix_sum[-1] + count)
            positions.append(pos)
            num_fruits.append(count)
            
        maximum = 0
        for i, pos in enumerate(positions):
            remaining = k - abs(startPos - pos)
            if remaining >= 0:
                if pos < startPos:
                    temp = max(pos + remaining, startPos)
                    j = bisect_left(fruits, [temp, float('inf')])
                    if j == len(fruits):
                        j -= 1
                    elif fruits[j][0] > temp:
                        j -= 1
                    maximum = max(maximum, prefix_sum[j + 1] - prefix_sum[i])
                else:
                    temp = min(pos - remaining, startPos)
                    j = bisect_left(fruits, [temp, 0])
                    if fruits[j][0] < temp:
                        j += 1
                    maximum = max(maximum, prefix_sum[i + 1] - prefix_sum[j])

        return maximum