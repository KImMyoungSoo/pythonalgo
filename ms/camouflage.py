def solution(clothes):
    answer = 1
    
    clothes_dic = dict(clothes)
    
    vals = clothes_dic.values()
    vals = list(set(vals))
    
    lens = []
    for i in vals :
        cnt = 0
        for val in clothes_dic.values() :
            if i == val :
                cnt = cnt + 1
        lens.append(cnt)
    
    lens = list(map(lambda a: a+1, lens))
    for i in lens :
        answer = answer * i
    
    return answer - 1
