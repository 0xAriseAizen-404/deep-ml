def valid_palindrome(s):
    # s: a string of lowercase letters
    # return True or False
    def is_pal(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return is_pal(left + 1, right) or is_pal(left, right - 1)
    return True