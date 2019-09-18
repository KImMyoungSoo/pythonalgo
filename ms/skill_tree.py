def solution(skill, skill_trees):
    answer = 0
    
    def check_skill(skill,tree):
        check = [0]*len(skill)
        bone = ''
        for i in tree :
            if i in skill :
                bone = bone + i
        
        for s in range(len(bone)) :
            if skill[s] != bone[s] :
                return False
        return True
    
    for tree in skill_trees :
        if check_skill(skill, tree) :
            answer = answer + 1
    return answer
