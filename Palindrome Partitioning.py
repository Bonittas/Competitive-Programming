class Solution(object):
    def partition(self, s):
        def backtrack(s, path, result):
            if not s:
                result.append(path[:])
                return

            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    path.append(s[:i])
                    backtrack(s[i:], path, result)
                    path.pop()

        result = []
        backtrack(s, [], result)
        return result
