def solution(rank, attendance):
   
    participants = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    participants.sort()

    a = participants[0][1]
    b = participants[1][1]
    c = participants[2][1]
   
    
    result = 10000 * a + 100 * b + c
    
    return result
