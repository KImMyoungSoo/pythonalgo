#https://programmers.co.kr/learn/courses/30/lessons/42585
def solution(arrangement):
    answer = 0
    stack = []
    switch = True
    for a in arrangement:
        if a == '(':
            stack.append(a)
            switch = True
        else:
            stack.pop()
            if switch == False:
                answer += 1
            else:
                answer += len(stack)
            switch = False
    return answer

