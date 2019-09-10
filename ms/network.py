#깊이/너비 우선탐색 네트워크

def solution(n, computers):
    answer = 0
    solu = [0]*n
    
    def visite(computers,solu,i):
        node = computers[i]
        for i in range(0,len(node)) :
            if node[i] == 1 and solu[i] == 0:
                solu[i] = 1
                visite(computers,solu,i)
        
    i = 0
    while 0 in solu :
        if solu[i] == 0 :
            visite(computers,solu,i)
            answer = answer + 1
        i = i + 1
    return answer
