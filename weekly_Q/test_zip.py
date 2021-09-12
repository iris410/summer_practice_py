marks = {'Physics':67, 'Maths':87}

print(marks.items())


list1 = [[('a',3)],[('b',5)]]
list2 = [('p',8)]
list3 = [[1],[123,4,6,8],[]]

for index,(k,v) in enumerate(list2):
    print(index)
    print(k)
    print(v)

each_len = [len(e) for e in list3]
print(min(each_len))

for e in range(0,0):
    print(f'testing range: {e}')

milk = [[1,2,3],[4,5,6]]
for i in milk:
    print(i)
