from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = [0] * (n + 1)
        ans = [0] * n
        common = 0

        for i in range(n):
            seen[A[i]] += 1
            if seen[A[i]] == 2:
                common += 1

            seen[B[i]] += 1
            if seen[B[i]] == 2:
                common += 1

            ans[i] = common

        return ans
