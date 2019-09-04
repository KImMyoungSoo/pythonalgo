#https://programmers.co.kr/learn/courses/30/lessons/42840
from collections import defaultdict
def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score_dict = defaultdict(int)

    for i,ans in enumerate(answers):
        if ans == one[i%len(one)]:
            score_dict[1] += 1
        if ans == two[i%len(two)]:
            score_dict[2] += 1
        if ans == three[i%len(three)]:
            score_dict[3] += 1

    '''
    for i in range(len(answers)):
        ans = answers[i]
        if ans == one[i%len(one)]:
            score_dict[1] += 1
        if ans == two[i%len(two)]:
            score_dict[2] += 1
        if ans == three[i%len(three)]:
            score_dict[3] += 1
    '''

    for name, score in score_dict.items():
        if score == max(score_dict.values()):
            answer.append(name)
    list.sort(answer)
    return answer

