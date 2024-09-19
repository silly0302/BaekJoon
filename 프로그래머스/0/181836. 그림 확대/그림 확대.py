def solution(picture, k):
    answer = []
    
    for row in picture:
        expanded_row = []

        for pixel in row:
            expanded_row.append(pixel * k)
        
        for _ in range(k):
            answer.append(''.join(expanded_row))
    
    return answer

            
        
  