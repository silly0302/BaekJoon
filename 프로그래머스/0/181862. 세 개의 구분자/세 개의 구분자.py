def solution(myStr): 
    
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    
 
    split_strings = myStr.split()
    
  
    if not split_strings:
        return ["EMPTY"]
    return split_strings

