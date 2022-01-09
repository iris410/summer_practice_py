import heapq
if __name__ == '__main__':
    #records = []
    records = {}
    #n=int(input()
    n=7
    names=['a','b','c','d','e','f','g']
    scores=[11,13,12,14,18,11,13]
    for i in range(n):
        if scores[i] not in records:
            records[scores[i]] = []
        records[scores[i]].append(names[i])


        #name = input()
        #score = float(input())
    l = list(records)
    heapq.heapify(l)#o(n)
    lowest = heapq.heappop(l)#o(logn)
    sec_lowest = heapq.heappop(l)
    print(records[lowest],records[sec_lowest])
    print(lowest,sec_lowest)
