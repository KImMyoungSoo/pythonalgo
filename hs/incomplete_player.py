#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    list.sort(participant)
    list.sort(completion)
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        if i == len(participant)-2:
            answer = participant[i+1]
            break
    # answer = list(set(participant) - set(completion))
    # answer = list(set(participant)^set(completion))
    # answer = set(participant).difference(completion).pop()
    return answer
