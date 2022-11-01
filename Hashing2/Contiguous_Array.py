#TimeComplexity: O(n)
#SpaceComplexity: O(1)
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={0:-1} # creating dictionary with 0 values
        max_length = 0
        Rsum = 0
        result = [0,0]
        for i in range(len(nums)):
            if nums[i] == 0:
                Rsum -= 1 # subtracting rsum with 1
            else:
                Rsum += 1 # adding rsum with 1
            
            if Rsum not in d:
                d[Rsum] = i # assigning rsum in dictionary with i
            else:
                if max_length < (i-d[Rsum]): # if maximum length is less than dictionary of rsum
                    max_length = i-d[Rsum] # assigning the value to maxlength
                    result[1] = i+1
                    result[0] = (i+1)-max_length # finding result of first by maxlength-i
        return max_length # returning maximum length
