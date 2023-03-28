class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        prefix_sum = [0]
        position = []
        num_fruits = []
        for pos, count in fruits:
            prefix_sum.append(prefix_sum[-1] + count)
            position.append(pos)
            num_fruits.append(count)

        maximum = 0

        for i, position in enumerate(position):
            remaining = k - abs(startPos - position)
            if remaining >= 0:
                if position < startPos:
                    temp = max(position + remaining, startPos)
                    j = bisect_left(fruits, [temp, inf])
                    if j == len(fruits) or fruits[j][0] > temp:
                        j -= 1
                    maximum = max(maximum, prefix_sum[j + 1] - prefix_sum[i])
                else:
                    temp = min(position - remaining, startPos)
                    j = bisect_left(fruits, [temp, 0])
                    if fruits[j][0] < temp:
                        j += 1
                    maximum = max(maximum, prefix_sum[i + 1] - prefix_sum[j])

        return maximum