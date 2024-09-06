def solution(my_string, queries):
    answer = list(my_string)
    for i,j in queries:
        while i < j:
            answer[i], answer[j] = answer[j], answer[i]
            i = i + 1
            j = j - 1
    return "".join(answer)