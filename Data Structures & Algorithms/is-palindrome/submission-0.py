class Solution:
    def isPalindrome(self, s):

        filtered = ""

        # giữ lại chữ và số
        for char in s:

            if char.isalnum():
                filtered += char.lower()

        # so sánh xuôi và ngược
        return filtered == filtered[::-1]