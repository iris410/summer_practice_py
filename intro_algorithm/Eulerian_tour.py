def create_tour1(nodes):
    #first way: connect each point one by one in order
    result = []
    for i in range(len(nodes)):
        each_path = (nodes[i],nodes[(i+1)%len(nodes)])
        result.append(each_path)
    print(result)

nodes = [1,2,3,4,5]
create_tour1(nodes)

num1 = [1,1,2,3]
num2 = [4,5]

new_nums1 = set(num1)
new_nums2 = set(num2)
print(new_nums1)
