#스택/큐 다리를 지나는 트럭

def minus(x):
    return x - 1

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = None
    
    con_bridge = []
    cnt = []
    
    while True :
        if not truck_weights and not con_bridge :
            break
        if cnt and cnt[0] == 0 :
            del cnt[0]
            del con_bridge[0]
        if truck_weights and sum(con_bridge) + truck_weights[0] <= weight :
            truck = truck_weights.pop(0)
            con_bridge.append(truck)
            cnt.append(bridge_length)
        # print(con_bridge)
        cnt = list(map(minus, cnt))
        answer = answer + 1
    return answer
