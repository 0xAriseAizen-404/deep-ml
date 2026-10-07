def add_two_numbers(l1, l2):
    # l1 and l2 are lists of digits in reverse order
    res = []
    carry = 0
    i = j = 0
    while i < len(l1) or j < len(l2) or carry:
        x = l1[i] if i < len(l1) else 0
        y = l2[j] if j < len(l2) else 0
        total = x + y + carry
        res.append(total % 10)
        carry = total // 10
        i += 1
        j += 1
    return res