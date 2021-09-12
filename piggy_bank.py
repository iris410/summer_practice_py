#bank:[1,2,3...], cost:4
def find_piggybank(bank,cost):
    ans = []
    for i,bank1 in enumerate(bank):
        for j,bank2 in enumerate(bank[i+1:]):
            if bank1 + bank2 == cost:
                pair = [i,j]
                ans.append(pair)
                print("{} and {}".format(bank1,bank2))
    print(ans)

def find_piggybank1(banks,cost):
    seen = [False for _ in range(cost+1)]
    index = [-1]*(cost+1)
    for i,bank1 in enumerate(banks):
        bank2 = cost - bank1
        if seen[bank2]:
            print(i,index[bank2])
            print(bank1, bank2)
        else:
            seen[bank1] = True
            index[bank1] = i


# def nested_loop(bank,cost):
#     for i in range(len(bank)):
#         for j in range(i+1,len(bank)):
#            total = bank[i] + bank[j]
#            print(total)
list = [100,0,6]
cost = 106
find_piggybank(list,cost)

print("-------")
find_piggybank1(list,cost)
