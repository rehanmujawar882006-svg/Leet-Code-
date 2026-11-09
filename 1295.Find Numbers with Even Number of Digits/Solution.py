class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        for i in nums:
            count=0
            
            while(i!=0):
                i=i/10
                count+=1
    
            if count%2==0:
                max_count+=1

        return max_count