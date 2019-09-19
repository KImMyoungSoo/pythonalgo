#https://programmers.co.kr/learn/courses/30/lessons/42628
import heapq
def solution(operations):
    answer, heap, rev_heap = [],[],[]

    for oper in operations:
        if oper[0] == "I":
            num = int(oper[2:])
            heapq.heappush(heap, num)
            heapq.heappush(rev_heap, -num)
        elif oper == "D 1" and rev_heap:
            heap.remove(-heapq.heappop(rev_heap))

        elif oper == "D -1" and heap:
            rev_heap.remove(-heapq.heappop(heap))
    if heap == [] and rev_heap == []:
        answer = [0,0]
    else:
        max = -heapq.heappop(rev_heap)
        min = heapq.heappop(heap)
        answer = [max, min]
    return answer
