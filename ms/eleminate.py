#짝지어 제거하기

def solution(s):
    answer = 1
    
    while s :
        token = True
        stack = ''
        for i in range(len(s)):
            if stack == '':
                stack = stack + s[i]
            else :
                temp = stack[-1]
                if temp == s[i] :
                    stack = stack[:-1]
                    token = False
        s = stack
        if token == True :
            answer = 0
            break
    return answer
