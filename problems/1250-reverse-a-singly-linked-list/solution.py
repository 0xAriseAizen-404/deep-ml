def reverse_linked_list(values, method="iterative"):
    # values: list of node values in head-to-tail order
    # method: 'iterative' or 'recursive'
    # return: list of node values after reversal
    if method == "iterative":
        res = []
        for val in values:
            res.insert(0, val)
        return res
    elif method == "recursive":
        def helper(arr):
            if len(arr) <= 1:
                return arr
            return [arr[-1]] + helper(arr[:-1])
        return helper(values)
    else:
        raise ValueError("method must be 'iterative' or 'recursive'")