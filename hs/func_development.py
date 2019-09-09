#https://programmers.co.kr/learn/courses/30/lessons/42586
import math
def solution(progresses, speeds):
    answer = []
    compare,count = math.ceil((100-progresses.pop(0))/speeds.pop(0)), 1
    while(True):
        days = math.ceil((100-progresses.pop(0))/speeds.pop(0))
        if compare >= days:
            count += 1
        else:
            compare = days
            answer.append(count)
            count = 1
        if progresses == []:
            answer.append(count)
            break
    return answer
