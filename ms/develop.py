# 스택/큐 기능개발

def solution(progresses, speeds):
    answer = []
    len_pro = len(progresses)

    while progresses :
        cnt = 0
        while progresses and progresses[0] >= 100 :
            cnt = cnt + 1
            del progresses[0]
            del speeds[0]
        if cnt != 0 :
            answer.append(cnt)
        for i in range(len(progresses)) :
            if progresses[i] < 100 :
                progresses[i] = progresses[i] + speeds[i]
    return answer
