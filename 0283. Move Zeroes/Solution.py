class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i] #Tuple Unpacking(swap Simultaneously)
                j+=1
        return nums

