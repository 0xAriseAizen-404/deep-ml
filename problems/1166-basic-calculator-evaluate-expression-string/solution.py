def evaluate_expression(s):
    # s is a string arithmetic expression
    # return the integer result
    nums = []
    ops = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply_operation():
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        if op == '+':
            nums.append(a + b)
        elif op == '-':
            nums.append(a - b)
        elif op == '*':
            nums.append(a * b)
        elif op == '/':
            nums.append(int(a / b))
        
    ind = 0
    while ind < len(s):
        ch = s[ind]
        if ch.isspace():
            ind += 1
            continue
        elif ch.isdigit():
            num = 0
            while ind < len(s) and s[ind].isdigit():
                num = num * 10 + int(s[ind])
                ind += 1
            nums.append(num)
            continue
        elif ch == '(':
            ops.append(ch)
        elif ch == ')':
            while ops and ops[-1] != '(':
                apply_operation()
            ops.pop()
        else:
            while ops and ops[-1] != '(' and precedence[ops[-1]] >= precedence[ch]:
                apply_operation()
            ops.append(ch)
        ind += 1
    
    while ops:
        apply_operation()
    
    return nums[-1]