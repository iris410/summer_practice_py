def naive_mul(x,y):
    a = x
    b = y
    c = 0
    while a > 0:
        c += b
        a -=1
    return c

print(naive_mul(2,3))

def recursive_naive(x,y):
    a = x
    b = y
    if a == 0:
        return 0
    else:
        return b + recursive_naive(a-1,b)
print(recursive_naive(3,4))
