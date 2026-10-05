def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    d1 = {}
    d2 = {}
    for val in list1:
        d1[val] = d1.get(val, 0) + 1
    for val in list2:
        d2[val] = d2.get(val, 0) + 1
    count = 0
    for val in d1:
        if d1[val] == 1 and d2.get(val, 0) == 1:
            count += 1
    return count