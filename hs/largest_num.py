#https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    answer = ''
    if len(numbers) == numbers.count(0):
        answer = '0'
    else:       
        numbers_str = list(map(str, numbers))
        answer = "".join(quick_sort(numbers_str))
    return answer

def quick_sort(list):
    if len(list) > 1:
        low, equal, high = [],[],[]
        pivot = list[len(list)//2]
        for ele in list:
            e, p= ele[0], pivot[0]
            if ele == pivot:
                equal.append(ele)
            else:
                # 첫자가 같을 경우
                if e == p:
                    e, p = get_standard_value_to_compare(ele, pivot)
                #  첫자와 끝자가 같을 경우
                if e == p:
                    e, p = average_element(ele), average_element(pivot)
                # 두 개 다 같은 숫자으로만 이루어진 경우
                if e == p:
                    equal.append(ele)
                if e > p:
                    low.append(ele)
                elif e < p:
                    high.append(ele)
        return quick_sort(low)+equal+quick_sort(high)
    else:
        return list
    
def get_standard_value_to_compare(ele, pivot):
    ele_char, pivot_char = '', ''
    ele_error_count, pivot_error_count = 0, 0
    ele_iter, pivot_iter = iter(ele), iter(pivot)
    count = 0
    while(1):       
        if ele_char != pivot_char:
            break
        if ele_error_count>1 and pivot_error_count>1:
            break
        ele_char, ele_error_count = get_next_char_and_error_count(ele_iter, ele_error_count)
        pivot_char, pivot_error_count = get_next_char_and_error_count(pivot_iter, pivot_error_count)
        if ele_error_count > 0 and pivot_error_count == 0:
            ele_char = ele[0]
        if pivot_error_count > 0 and ele_error_count == 0:
            pivot_char = pivot[0]
        
        count += 1
    if ele_char == '' and pivot_char == '':
        ele_char, pivot_char = ele[0], pivot[0]
        
    return ele_char, pivot_char

def get_next_char_and_error_count(s_iter, error_count):
    next_char = ''
    try:
        next_char = next(s_iter)
    except StopIteration:
        error_count += 1
    return next_char, error_count        

def average_element(num):
    result, ele_sum = 0,0
    digit = len(num)
    if digit > 1:
        for i in range(digit):
            ele_sum += int(num[i])
        result = ele_sum/digit
    else:
        result = num
    return str(result)


