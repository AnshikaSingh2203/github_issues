def isValid(s):
    # Dictionary to match opening and closing brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Pop the topmost element if stack is not empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the top of the stack doesn't match the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # Push the opening bracket onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched
    return not stack

s="[({[})]"
print(isValid(s))
