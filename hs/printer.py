#https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0
    while(True):
        pop = priorities[0]
        location %= len(priorities)
        if pop == max(priorities):
            answer += 1
            if location  == 0:
                break
            priorities.pop(0)
            location -= 1
        else:
            priorities.pop(0)
            priorities.append(pop)
            location -= 1
    return answer
