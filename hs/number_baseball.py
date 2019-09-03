#https://programmers.co.kr/learn/courses/30/lessons/42841
import itertools
def solution(baseball):
    num = ['1','2','3','4','5','6','7','8','9']
    answer = 0
    permu = [''.join(x) for x in itertools.permutations(num,3)]

    for p in permu:
        for b in baseball:
            if isSatisfied(b,p) == False:
                break
            if b == baseball[-1]:
                answer +=1
    return answer

def isSatisfied(b, compare_num):
    strike = 0
    ball = 0
    for i,j in zip(str(b[0]), compare_num):
        if i == j:
            strike +=1
        if compare_num.find(i) >= 0:
            ball += 1
    if strike != b[1]:
        return False
    if (ball-strike) != b[2]:
        return False
    else:
        return True
