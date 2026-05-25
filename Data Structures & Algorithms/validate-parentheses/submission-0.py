class Solution:
    def isValid(self, s):

        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            # nếu là dấu đóng
            if char in pairs:

                # stack rỗng hoặc không khớp
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

            else:
                # dấu mở thì đưa vào stack
                stack.append(char)

        return len(stack) == 0