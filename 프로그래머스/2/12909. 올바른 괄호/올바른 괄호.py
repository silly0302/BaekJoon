def solution(s):
    stck = []
    for i in range(len(s)):
        if not stck and s[i] == "(":
            stck.append(s[i])
            continue
        elif not stck and s[i] == ")":
            return False
        top = stck[-1]
        if top == s[i]:
            stck.append(s[i])
        elif top != s[i]:
            stck.pop()
        
    if not stck:
        return True
    return False