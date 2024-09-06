def solution(code):
    mode = 0
    ret = []
    
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = 1 - mode  # mode를 0에서 1로, 1에서 0으로 전환
        else:
            if mode == 0 and idx % 2 == 0:
                ret.append(code[idx])
            elif mode == 1 and idx % 2 == 1:
                ret.append(code[idx])
    
    ret = ''.join(ret)
    if ret == "":
        return "EMPTY"
    
    return ret



