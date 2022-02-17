# backtracking
# recursion + termination check
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        temp = []

        def addBracket(numOpen, numClosed):
            # termination check
            if numOpen == n and numClosed == n:
                result.append(''.join(temp))
                return

            # recurse next
            if numOpen < n:
                temp.append('(')
                addBracket(numOpen+1, numClosed)
                temp.pop()

            if numClosed < numOpen:
                temp.append(')')
                addBracket(numOpen, numClosed+1)
                temp.pop()

        addBracket(0, 0)

        # print(result)
        return result

# test = Solution()
# test.generateParenthesis(3)