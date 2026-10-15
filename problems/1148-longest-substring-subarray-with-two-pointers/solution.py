def longest_unique_substring(s):
    freq = [-1] * 128
    left = 0
    max_len = 0
    for right in range(len(s)):
        ch = ord(s[right])
        if freq[ch] >= left:
            left = freq[ch] + 1
        freq[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len