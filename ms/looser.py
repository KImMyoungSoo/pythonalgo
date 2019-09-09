def solution(participant, completion):
    answer = ''
    completion.append('zzzzz')
    sort_p = sorted(participant)
    sort_c = sorted(completion)
    for i in range(0,len(sort_p)) :
        if sort_p[i] != sort_c[i] :
            answer = sort_p[i]
            break
    return answer
