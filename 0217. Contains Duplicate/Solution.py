class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x=set()
        for i in nums:
            if i in x:
                return True
            x.add(i)
        return False