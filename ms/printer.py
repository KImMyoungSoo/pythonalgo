def solution(priorities, location):
    answer = 0
    priorities[location] = str(priorities[location])
    
    while priorities :
        token = False
        # print(priorities)
        # print(answer)
        waiting = priorities[0]
        for i in range(1,len(priorities)):
            if int(waiting) < int(priorities[i]) :
                token = True
                del priorities[0]
                priorities.append(waiting)
                break
        if type(priorities[0]) is str and (not token):
            answer = answer + 1
            break
        if not token :
            del priorities[0]
            answer = answer + 1
    return answer
