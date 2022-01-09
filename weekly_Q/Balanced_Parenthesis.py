#a string of some "(" and  ")" as input,
#output should be an integer number to represent the longest contiguous
#balanced parenthesis that you can understand from my test example below

def balanced_count(string):
    #left_p_count = 0
    string_list = []
    max_count = 0
    count = 0

    for i in range(len(string)):
        ch = string[i]
        if ch == "(":
            #left_p_count += 1
            string_list.append(i)
        if ch == ")":
            # if left_p_count > 0:
            #     left_p_count -= 1
            if len(string_list) > 0:
                string_list.pop()
                count += 1
            else:
                #print(count)
                max_count = max(count, max_count)
                count = 0
    max_count = max(count, max_count)
    #print(count)
    return max_count*2


test1 = ")(())())))((((()" # equal 6
print(balanced_count(test1))
test2 = "((())())"
print(balanced_count(test2))# =8
test3 = "(()"
print(balanced_count(test3))# =2
test4 = "()))"
print(balanced_count(test4))# =2
test5 = "(((()))"
print(balanced_count(test5))# =6
test6 = "()((())(())"
print(balanced_count(test6))# =8
#terminal ans is 10 (more left parenthesis than other test)
