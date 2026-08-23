class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [x for x in nums if x > 0]
        negative = [x for x in nums if x < 0]
        result = []
        for positives , negative in zip (positives , negative ):
            result.append(positives)
            result.append(negative)
        return result    

        