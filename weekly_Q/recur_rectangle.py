# input: 2-d list
# output: biggest sum within area
def solution(two_d_list):
    if len(two_d_list) == 0:
        return 0
    else:
        # line_num is used to record all indexes of lines with shortest length.(shortest pillers)
        line_num = []
        for i, e in enumerate(two_d_list):
            if len(e) == shortest(two_d_list):
                line_num.append(i)
                # print(i)
        pre = 0
        cur = 0
        sub_area = []
        for e in line_num:#[0,1]
            sub_line = []
            cur = e
            for num in range(pre,cur):
                sub_line.append(num)
            if sub_line:
                sub_area.append(sub_line)
            pre = cur+1

        buttom_part = []
        for num in range(pre,len(two_d_list)):
            buttom_part.append(num)
        if buttom_part:
            sub_area.append(buttom_part)

        lists = []
        for e in sub_area:
            each_sum_lines = []
            for i in e:
                each_sum_lines.append(two_d_list[i])
            lists.append(each_sum_lines)

        results = []
        for e in lists:
             results.append(solution(e))

        common_area = sum_area(two_d_list)

        print(f'input: {two_d_list},\nindex_based_sub_area: {sub_area},\n sub_areas: {lists},\n results: {results},\n common_area_size: {common_area}\n')

        return max(results + [common_area])


        # return sub_area
        # max(max_sum_of_sub_areas, sum)
        #max(solution([[1,3]]), solution([[1,2],[3,4]]), solution([[3,4,5], [1,2],[4,5]]), common_base)


def shortest(two_d_list):
    each_len = [len(e) for e in two_d_list]
    return min(each_len)

def sum_area(two_d_list):
    sum = 0
    for i in range(len(two_d_list)):
        for j in range(shortest(two_d_list)):
            sum += two_d_list[i][j]
    return sum





# list1 = [[1, 3, 2, 2], [2, 1, 2, 3], [4, 2, 3], [1, 1, 2, 17, 14], [3, 1, 2, 2]]
# ans = solution(list1)
# print(ans)
print('----test 1-----')
test_list1 = [[1, 3, 2, 2], [2, 1, 2, 3], [4, 2, 3], [1, 1, 2, 17, 14], [3, 1, 2, 2]]
print(solution(test_list1))

print('----test 2-----')
test_list2 = [[1, 2], [3, 4, 5, 6], [7, 8], [9]]
print(solution(test_list2))

print('----test 3-----')
test_list2 = [[1], [3, 4, 5, 6], [7, 8], [9,10]]
print(solution(test_list2))

print('----test 4-----')
test_list2 = [[1,2], [3, 4, 5, 6], [7, 8], [100]]
print(solution(test_list2))
