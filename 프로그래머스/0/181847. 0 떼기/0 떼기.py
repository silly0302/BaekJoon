def solution(n_str):
    ns = list(n_str)
    for i in range(len(ns)):
        if ns[0] == "0":
            del ns[0]
        else:
            break
    ns = "".join(ns)
    return ns