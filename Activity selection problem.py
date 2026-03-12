from heapq import heappop, heappush

def select_ativity(s, f):
    ans = []
    p = []

    for i, j in zip(s, f):
        heappush(p, (j, i))

    item = heappop(p)
    start = item[1]
    end = item[0]
    ans.append(item)

    while p:
        item = heappop(p)
        start = item[0]
        end = item[1]
        ans.append(item)

    for f, s in ans:
        print(s, f)

s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 8]
select_ativity(s, f)