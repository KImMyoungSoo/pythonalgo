#https://programmers.co.kr/learn/courses/30/lessons/42842
import math
def solution(brown, red):
    answer = []
    i= math.ceil(math.sqrt(brown+red))
    j=i
    while(True):
        if j == 0:
            j = i
            i += 1
        if i*j == brown+red and (i-2)*(j-2) == red:
            answer.append(i)
            answer.append(j)
            break
        j -= 1
    return answer
