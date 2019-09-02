#https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    result = 0
    while(scoville[0] < K):
        try : 
            result = heapq.heappop(scoville) + 2*heapq.heappop(scoville)
        except Exception as e:
            break
        heapq.heappush(scoville, result)
        answer +=1
    if result < K:
        answer = -1
    return answer
