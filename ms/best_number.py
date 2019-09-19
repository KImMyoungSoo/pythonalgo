# 가장큰수

def solution(numbers):
    answer = ''
    numbers = quick_max_sort(numbers)
    for i in numbers:
        answer = answer + str(i)
    answer = str(int(answer))
    return answer

def quick_max_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    lenp = len(numbers) // 2
    pivot = numbers[lenp]
    lesser_arr, greater_arr = [], []
    # print(pivot)
    for i in range(len(numbers)):
        if i == lenp:
            continue
        if len(str(pivot)) == len(str(numbers[i])):
            if(numbers[i] > pivot):
                greater_arr.append(numbers[i])
            else :
                lesser_arr.append(numbers[i])
        else :
            if(int(str(numbers[i])+str(pivot)) > int(str(pivot)+str(numbers[i]))) :
                greater_arr.append(numbers[i])
            else :
                lesser_arr.append(numbers[i])
    return quick_max_sort(greater_arr)+ [pivot] + quick_max_sort(lesser_arr)
