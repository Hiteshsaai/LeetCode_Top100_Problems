class Solution:
    def isValid(self, s):
        ## Time O(n) || Space O(n)
        if not s:
            return False

        closeBrackets = {"}": "{", ")": "(", "]": "["}

        stack = []

        for bracket in s:

            if not stack or bracket not in closeBrackets:
                stack.append(bracket)
            elif closeBrackets[bracket] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0


if __name__ == "__main__":

    s1 = "()[]{}"
    s2 = "((([{}]))("
    print(Solution().isValid(s1))
    print(Solution().isValid(s2))
