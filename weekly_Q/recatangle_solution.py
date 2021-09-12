def solution1(begin,end,two_d_list):
    smallest = 100000
    smallest_index = -1
    if (end - begin <= 1):
        return sum(two_d_list[begin]), begin , end

    for i in range(begin,end):
        if (len(two_d_list[i]) < smallest):
            smallest_index = i
            smallest = len(two_d_list[i])
    #begin-> smallest_index -> end
    s1,b1,e1 = solution1(begin, smallest_index, two_d_list)
    s2,b2,e2 = 0,0,0
    if (smallest_index+1 < end):
        s2,b2,e2 = solution1(smallest_index+1, end, two_d_list)
    s3,b3,e3 = area(begin, end, two_d_list, smallest),begin,end

    max_area = max(s1,s2,s3)
    if max_area == s1:
        return s1,b1,e1
    elif max_area == s2:
        return s2,b2,e2
    else:
        return s3,b3,e3

def area(begin, end, two_d_list, h):
    s = 0
    for i in range(begin,end):
        for j in range(h):
            s += two_d_list[i][j]
    return s

def solution(two_d_list):
    result, index_begin, index_end = solution1(0,len(two_d_list),two_d_list)
    min_height = 100000
    for i in range(index_begin,index_end):
        min_height = min(min_height,len(two_d_list[i]))
    return [result,[index_begin,0],[index_end-1,min_height-1]]


two = [[1, 3, 2, 2], [2, 1, 2, 3], [4, 2, 3], [1, 1, 2, 17, 14], [3, 1, 2, 2]]
ans = solution(two)
print(ans)

two1 = [[1, 2], [3, 4, 5, 6], [7, 8], [9]]
ans = solution(two1)
print(ans)
