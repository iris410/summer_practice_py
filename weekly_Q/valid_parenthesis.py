def valid_parenthesis(string):
    #parenthesis_list = []
    left_p_count = 0
    for ch in string:
        if ch == "(":
            left_p_count +=1
            #parenthesis_list.append(ch)
        if ch == ")":
            if left_p_count > 0:
                left_p_count -= 1
            #if len(parenthesis_list) > 0:
                #parenthesis_list.pop()
            else:
                return False
    if left_p_count > 0: 
    #if len(parenthesis_list) > 0:
        return False
    else:
        return True

test1 = "()(())()"# True
test2 = "()())"# False
test3 = "(()"# False
test4 = "((())())" # True
test5 = ""# True
print(valid_parenthesis(test1))
print(valid_parenthesis(test2))
print(valid_parenthesis(test3))
print(valid_parenthesis(test4))
print(valid_parenthesis(test5))
