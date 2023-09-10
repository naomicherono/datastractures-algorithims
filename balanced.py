def is_balanced(expression):   
    stack = []  # Initialize an empty stack to keep track of opening brackets
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}  # Define pairs of matching brackets
    
    # Iterate through each character in the expression
    for char in expression:
        if char in opening_brackets:  # If the character is an opening bracket
            stack.append(char)  # Push it onto the stack
        elif char in closing_brackets:  # If the character is a closing bracket
            if not stack or stack[-1] != bracket_pairs[char]:
                # If the stack is empty or the last element in the stack doesn't match the corresponding opening bracket
                return False  # The expression is not balanced
            stack.pop()  # Pop the last element from the stack to match the opening bracket
        
    # After processing all characters, check if there are any unmatched opening brackets left
    return len(stack) == 0  # If the stack is empty, the expression is balanced

# Output
print(is_balanced("()"))  # True
print(is_balanced("()[]{}"))  # True
print(is_balanced("(]"))  # False
print(is_balanced("([)]"))  # False
print(is_balanced("{[]}"))  # True