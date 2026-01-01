def solve_jobs(T, L):
    N = len(T)
    jobs = []
    for i in range(N):
        jobs.append((i + 1, T[i], L[i]))

    for i in range(N):
        for j in range(0, N - i - 1):
            job1 = jobs[j]
            job2 = jobs[j+1]
            if job1[2] * job2[1] < job2[2] * job1[1]:
                jobs[j], jobs[j+1] = jobs[j+1], jobs[j]
            elif job1[2] * job2[1] == job2[2] * job1[1]:
                if job1[0] > job2[0]:
                    jobs[j], jobs[j+1] = jobs[j+1], jobs[j]

    sequence = [job[0] for job in jobs]
    return sequence