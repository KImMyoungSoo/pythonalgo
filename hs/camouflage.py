#https://programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict
from itertools import combinations
def solution(clothes):
    answer = 0
    clothes_dict = defaultdict(int)
    for cloth in clothes:
        clothes_dict[cloth[1]] += 1
    nums = clothes_dict.values()
    if len(nums) == 1:
        answer += sum(nums)
    else:
        answer = multiply_list(map(lambda x:x+1, nums))-1
    '''
    if len(nums)>1:
        answer += multiply_list(nums)
    for i in range(2,len(nums)):
        for com in combinations(clothes_dict.values(), i):
            # answer += reduce(lambda x, y : x*y, com)
            answer += multiply_list(com)
    '''
    return answer


def multiply_list(list):
    result = 1
    for num in list:
        result *= num
    return result
