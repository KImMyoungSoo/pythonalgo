from itertools import permutations

def enclose(unit,solu) :
    num = ''
    for i in unit:
        num = num + i
    num = int(num)
    solu.append(num)
    return solu
        
def check_prime(n): 
    if n < 2: 
        return False
    if n is 2: 
        return True
    if n % 2 is 0:
        return False
    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i is 0:
            return False
    return True

def solution(numbers):
    answer = 0
    perm = []
    for i in range(1,len(numbers)+1) :
        temp = list(map(list, permutations(numbers, i)))
        perm = perm + temp
    solu = []
    for i in perm :
        solu = enclose(i,solu)
    solu = list(set(solu))
    for i in solu :
        if check_prime(i) :
            answer = answer + 1
    return answer
