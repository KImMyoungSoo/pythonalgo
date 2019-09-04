def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    cnt_one = 0
    cnt_two = 0
    cnt_thr = 0
    
    # 리스트 길이 확장
    while len(answers) > len(one) :
        one = one + one
    while len(answers) > len(two) :
        two = two + two
    while len(answers) > len(thr) :
        thr = thr + thr
    
    #counting correct answers
    for i in range(0,len(answers)) :
        if answers[i] == one[i] :
            cnt_one = cnt_one + 1
        if answers[i] == two[i] :
            cnt_two = cnt_two + 1
        if answers[i] == thr[i] :
            cnt_thr = cnt_thr + 1
    
    # compare three students
    if cnt_one == cnt_two and cnt_two == cnt_thr :
        answer.append(1)
        answer.append(2)
        answer.append(3)
    elif cnt_one == cnt_two :
        if cnt_one > cnt_thr :
            answer.append(1)
            answer.append(2)
        else :
            answer.append(3)
    elif cnt_two == cnt_thr :
        if cnt_one > cnt_two :
            answer.append(1)
        else :
            answer.append(2)
            answer.append(3)
    elif cnt_one == cnt_thr :
        if cnt_one > cnt_two :
            answer.append(1)
            answer.append(3)
        else :
            answer.append(2)
    else :
        if cnt_one > cnt_two :
            if cnt_two > cnt_thr :
                answer.append(1)
            else :
                if cnt_one > cnt_thr:
                    answer.append(1)
                else :
                    answer.append(3)
        elif cnt_one < cnt_two :
            if cnt_two < cnt_thr :
                answer.append(3)
            else :
                answer.append(2)
    return answer
