def solution(myString, pat):
    longest_substring = ""
    
    for i in range(len(myString)):

        substring = myString[:i+1]
        
        if substring.endswith(pat):
            longest_substring = substring
    
    return longest_substring
