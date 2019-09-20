#https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    answer = 0
    for i, tri in enumerate(triangle[1:]):
        for j in range(len(tri)):
            if j == 0:
                triangle[i+1][j] += triangle[i][j]
            elif j == len(tri)-1:
                triangle[i+1][j] += triangle[i][j-1]
            else:
                if triangle[i][j-1] >= triangle[i][j]:
                    triangle[i+1][j] += triangle[i][j-1]
                else:
                    triangle[i+1][j] += triangle[i][j]
    answer = max(triangle[-1])

    return answer
