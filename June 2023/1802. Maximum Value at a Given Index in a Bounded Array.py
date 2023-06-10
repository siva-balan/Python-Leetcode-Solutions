class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:


        # for i in range((maxSum-n+1),0,-1):
        #     total = 0
        #     for j in range(n):
        #         if total > maxSum:
        #             break
        #         if j <= index:
        #             if (i - index + j) > 0:
        #                 total += (i - index + j)
        #             else:
        #                 total +=1
        #         else:
        #             if (i + index - j) > 0:
        #                 total += (i+ index - j)
        #             else:
        #                 total +=1
        #     if total <= maxSum:
        #         return i

        def calc_sum(cnt, end):
            if cnt == 0:
                return 0
            start = max(end - cnt, 0)
            sum1 = end * (1 + end) // 2
            sum2 = start * (1 + start) // 2
            return sum1 - sum2

        maxSum -= n
        l, r = 0, maxSum
        while l <= r:
            mid = (l + r) // 2
            left_sum = calc_sum(index + 1, mid)
            right_sum = calc_sum(n - index - 1, mid - 1)
            if left_sum + right_sum <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return l
