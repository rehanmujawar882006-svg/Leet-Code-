class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for choice in s:
            if choice in pairs:
                if not stack or stack.pop() != pairs[choice]:
                    return False
            else:
                stack.append(choice)

        return len(stack) == 0