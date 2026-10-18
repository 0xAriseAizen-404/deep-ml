def min_remove_to_make_valid(s):
    # s is a string of lowercase letters, '(' and ')'
    # Return a valid string after removing the fewest parentheses
    stack = []
    remove = set()
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                remove.add(i)
        else:
            pass
    remove.update(stack)
    return ''.join(ch for i, ch in enumerate(s) if i not in remove)