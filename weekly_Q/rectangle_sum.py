def sum_two_points(list,length,start_line,current_line):
    sum = 0
    for line_num in range(start_line,current_line+1):
        for num in range(0,length):
            sum += list[line_num][num]
    return sum

def rectangle(list):
    stack_line_number = [-1,0]
    current_line = 0
    max_sum = 0
    for e in range(0,len(list)):
        if len(list[e+1]) >= len(list[e]):
            stack_line_number.append(e+1)
            current_line = e+1
        else:
            stack_line_number.pop()
            sum_two_points(list,)
