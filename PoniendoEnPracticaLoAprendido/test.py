class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        controlador = True
        for i in range(len(s)):
            if s[i] == "(" and ")" in s:
                s = s[1:]
                if ")" in s:
                    return True
                else:
                    return False and controlador == False
            elif s[i] == "[":
                s = s[1:]
                if "]" in s:
                    return True
                else:
                    return False and controlador == False
            elif s[i] == "{":
                s = s[1:]
                if "}" in s:
                    return True
                else:
                    return False and controlador == False
            if controlador == False:
                return False
            else:
                return True

solution = Solution()
print(solution.isValid("()"))

