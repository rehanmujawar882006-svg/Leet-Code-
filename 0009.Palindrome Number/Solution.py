class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original=x
        digit =0
        while(x>0):
            reminder=x%10
            digit=digit*10+reminder
            x=x/10
        if(original==digit):
            return True
        else:
            return False
        