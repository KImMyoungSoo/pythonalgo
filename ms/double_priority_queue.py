#이중우선큐

import heapq

def solution(operations):
    answer = []
    incre = []
    decre = []

    def checking(element, incre, decre) :
        sign = element[0]
        num = int(element[2:])

        if sign == 'I' :
            heapq.heappush(incre, num)
            heapq.heappush(decre, -num)
        else :
            if not incre and not decre :
                return incre, decre
            if num == 1 :
                temp = -heapq.heappop(decre)
                incre.remove(temp)
            else :
                temp = -heapq.heappop(incre)
                decre.remove(temp)
        return incre, decre

    for i in operations :
        incre, decre = checking(i, incre, decre)

    if not incre and not decre :
        incre.append(0)
        decre.append(0)

    answer.append(-decre[0])
    answer.append(incre[0])

    return answer
