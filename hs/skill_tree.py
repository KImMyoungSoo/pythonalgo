# https://programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for s_tree in skill_trees:
        prev_c_i = s_tree.find(skill[0])
        is_correct = True
        for c in skill[1:]:
            cur_c_i = s_tree.find(c)
            if prev_c_i == -1 and cur_c_i != -1:
                is_correct = False
                break
            if prev_c_i > cur_c_i and cur_c_i != -1:
                is_correct = False
                break
            prev_c_i = cur_c_i
        if is_correct == True:
            answer += 1
    return answer
