def solution(s):
    stck = []

    for i in range(len(s)):
        if not stck:
            stck.append(s[i])
            continue

        top = stck[-1]
        if top == s[i]:
            stck.pop()
        else:
            stck.append(s[i])

    if not stck:
        return 1
    return 0