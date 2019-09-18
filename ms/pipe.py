# 스킬트리

def solution(arrangement):
    answer = 0
    stack = []
    
    is_open = True
    
    for i in arrangement :
        if i == '(' :
            stack.append(i)
            is_open = True
        else :
            stack.pop()
            if is_open :
                answer = answer + len(stack)
                is_open = False
            else :
                answer = answer + 1
                 
    return answer
