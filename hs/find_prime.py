#https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
import math
def solution(numbers):
    answer = 0
    perm = [''.join(j) for i in range(len(numbers)) for j in permutations(numbers, i+1)]
    perm = list(set(list(map(int,perm))))
    for num in perm:
        if isPrime(num) == True:
            answer += 1
    return answer

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
