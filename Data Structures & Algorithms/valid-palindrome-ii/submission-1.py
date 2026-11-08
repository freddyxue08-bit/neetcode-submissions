class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(lo: int, hi: int) -> bool:
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Delete one character: skip the left one or the right one
                return (is_palindrome(left + 1, right) or
                        is_palindrome(left, right - 1))
            left += 1
            right -= 1
        return True