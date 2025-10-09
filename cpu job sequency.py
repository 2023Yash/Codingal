def job(arr, t):
    arr.sort(key = lambda x:x[2], reverse = True)
    result = [False] * t
    job = ["-1"] * t
    profit = 0
    for i in range(len(arr)):
        job_id = arr[i][0]
        deadline =  arr[i][1]
        profit_loop = arr[i][2]

        for j in range(min(t, deadline) -1, -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = job_id
                profit += profit_loop
                break
    print(job)
    print(profit)

arr = [
    ['a', 2,100],
    ['b', 1,90],
    ['c', 2,27],
    ['d', 1,25],
    ['e', 3,15]
]

job(arr, 3)