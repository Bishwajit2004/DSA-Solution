class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        reachable_count = 0

        for index in range(1, n):
            if index - minJump >= 0 and reachable[index - minJump]:
                reachable_count += 1

            if index - maxJump - 1 >= 0 and reachable[index - maxJump - 1]:
                reachable_count -= 1

            if s[index] == "0" and reachable_count > 0:
                reachable[index] = True

        return reachable[-1]
