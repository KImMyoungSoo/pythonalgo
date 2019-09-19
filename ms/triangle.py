#Dynamic Programming / 정수 삼각형

def solution(triangle):
    maxi = []

    for row in triangle :
        first = []
        if not maxi :
            first.append(row[0])
        else :
            for idx, num in enumerate(row) :
                if idx == 0 :
                    first.append(maxi[-1][idx] + num)
                elif idx == len(row) - 1 :
                    first.append(maxi[-1][-1] + num)
                else :
                    first.append(max(maxi[-1][idx-1], maxi[-1][idx]) + num)
        maxi.append(first)
    return max(maxi[-1])
