def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
           
            pass

    return not stack


expression1 = "([]{})"
expression2 = "([)]"

print(is_balanced(expression1)) 

