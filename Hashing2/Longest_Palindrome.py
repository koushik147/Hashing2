#TimeComplexity: O(n)
#SpaceComplexity: O(1)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set()# creating set
        count = 0
        for i in s:
            if i not in hashset: 
                hashset.add(i) # adding in set
            else:
                hashset.remove(i) # remove from set
                count += 2
        if len(hashset) != 0: # if length of set is not equal to 0
            count += 1
        return count # returning count
