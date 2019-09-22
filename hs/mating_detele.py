#https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    save_stack = []
    for c in s:
        if save_stack and save_stack[-1] == c:
            save_stack.pop()
        else:
            save_stack.append(c)
    if save_stack:
        return 0
    else:
        return 1

#try2 - complex code
'''
    save_stack = []
    for i, c in enumerate(s):
        if i == len(s)-1:
            if len(save_stack) == 1 and save_stack[-1] == c:
                return 1
            else:
                return 0
        else:
            if save_stack and save_stack[-1] == c:
                save_stack.pop()
            else:
                save_stack.append(c)
'''

#try1 - Efficiency test failed
'''
    save_stack = []
    while(True):
        if s == '':
            if save_stack == []:
                return 1
            else:
                return 0
        else:
            if save_stack and save_stack[-1] == s[0]:
                save_stack.pop()
                s = s[1:]
            else:
                save_stack.append(s[0])
                s = s[1:]
'''
