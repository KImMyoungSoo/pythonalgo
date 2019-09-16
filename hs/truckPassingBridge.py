#https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0]*(bridge_length)
    total_w = 0
    while True:
        if total_w == 0 and truck_weights == []:
            break
        truck_w = queue.pop(0)
        if truck_w != 0:
            total_w -= truck_w
        if truck_weights != [] and (total_w+truck_weights[0]) <= weight:
            truck_w = truck_weights.pop(0)
            queue.append(truck_w)
            total_w += truck_w
        else:
            queue.append(0)
        answer += 1


    return answer
