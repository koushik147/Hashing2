class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={0:-1}
        max_length = 0
        Rsum = 0
        result = [0,0]
        for i in range(len(nums)):
            if nums[i] == 0:
                Rsum -= 1
            else:
                Rsum += 1
            
            if Rsum not in d:
                d[Rsum] = i
            else:
                if max_length< (i-d[Rsum]):
                    max_length = i-d[Rsum]
                    result[1] = i+1
                    result[0] = (i+1)-max_length
        return max_length