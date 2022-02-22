class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        cnt = 0

        for _ in range(32):
            if res & 1 == 1:
                cnt += 1
            res = res >> 1

        return cnt