def longest_balanced(string):
    stack = [] # O(n) space.
    longest = 0
    for i, char in enumerate(string): # O(n) time.
        if char == '(':
# Remember index of the opening parenthesis.
            stack.append(i)
        elif char == ')':
# If we previously encountered an opening parenthesis,
            if stack:
# We recall the index of the last one that hasn't been matched yet.
                open_i = stack.pop()
# And compute the distance between them.
# All the parentheses between these two must have been balanced!
                length = i - open_i + 1
# Keep track of the longest encountered so far
                if length > longest:
                   longest = length
# And return it.
    return longest

test1 = ")(())())))((((()" # equal 6
print(longest_balanced(test1))
test2 = "((())())"
print(longest_balanced(test2))# =8
test3 = "(()"
print(longest_balanced(test3))# =2
test4 = "()))"
print(longest_balanced(test4))# =2
test5 = "(((()))"
print(longest_balanced(test5))# =6
test6 = "()((())(())"
print(longest_balanced(test6))# =4
