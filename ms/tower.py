#스택/큐 탑

def solution(heights):
    answer = []
    token = True

    heights.reverse()

    for i in range(0,len(heights)) :
        token = False
        for j in range(i,len(heights)) :
            if heights[j] > heights[i] :
                answer.append(len(heights) - j)
                token = True
                break
        if token == False :
            answer.append(0)
    answer.reverse()
    return answer
