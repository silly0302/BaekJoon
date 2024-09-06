def solution(arr, queries):
    tmp = 0
    for s,e,k in queries:
        tmp = 0
        for i in arr[s:e+1]:
            if (s+tmp) % k == 0:
                arr[s+tmp] += 1 
            tmp += 1
    return arr