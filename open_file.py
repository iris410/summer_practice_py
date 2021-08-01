# f = open("test.txt","w")
# file_data = f.write("Hello!! You've read the contents of this file!")
# f.close()
#
# f1 = open("test.txt","r")
# file_data = f1.read()
# print(file_data)
# for line in f1:
#     print(line, end = "")
# list(f1)
# f1.readlines()
# f1.readline()
# f1.close()
#
# with open("test.txt","r") as f:
#     print(f.read(2))
#     print(f.read(4))
#     file_data = f.read()
#
# print(file_data)
#
#
def longest_balanced(string):
    l_parenthesis = []
    count = 0
    max_count = 0
    for ch in string:
        if ch == "(":
            l_parenthesis.append("(")
        if ch == ")":
            if len(l_parenthesis) > 0:
                l_parenthesis.pop()
                count += 1
            else:
                max_count = max(max_count,count)
                count = 0
    max_count = max(max_count,count)
    return (max_count * 2)
string1 = "(()((("
print(longest_balanced(string1))
