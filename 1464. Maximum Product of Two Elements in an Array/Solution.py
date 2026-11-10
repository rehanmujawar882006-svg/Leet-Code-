class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        y=0
        for i in nums:
            if i>x:
                y=x
                x=i
            elif i>y:
                y=i
        return (x-1)*(y-1)