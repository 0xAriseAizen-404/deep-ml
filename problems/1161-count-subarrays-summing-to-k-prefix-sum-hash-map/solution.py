from math import inf

def count_and_longest_subarrays(nums, k):
    # nums: list of ints, k: int
    # return a tuple (count, longest)
    mapp = {0: (-1, 1)} # (index, count)
    summ = count = longest = 0
    for i, num in enumerate(nums):
        summ += num
        remaining = summ - k
        if remaining in mapp:
            count += mapp[remaining][1]
            longest = max(longest, i - mapp[remaining][0])
        if summ in mapp:
            mapp[summ] = (mapp[summ][0], mapp[summ][1] + 1)
        else:
            mapp[summ] = (i, 1)
    return count, longest