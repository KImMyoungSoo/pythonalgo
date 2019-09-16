#https://programmers.co.kr/learn/courses/30/lessons/42588
def solution(heights):
    answer = []
    while(heights):
        sender = heights.pop()
        for i, tower in reversed(list(enumerate(heights))):
            if tower > sender:
                answer.insert(0, i+1)
                break
            if i == 0:
                answer.insert(0, 0)
        if heights == []:
            answer.insert(0, 0)
            
    return answer
