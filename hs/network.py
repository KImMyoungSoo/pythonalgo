#https://programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    answer = 0
    graph_dict = {}
    ele_list = set(range(1,n+1))

    for i in range(n):
        link_list = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                link_list.append(j+1)
        graph_dict[i+1] = link_list
    while ele_list:
        ele_list -= set(DFS(graph_dict, ele_list.pop()))
        answer +=1

    return answer

def DFS(graph, start):
    to_visit = [start]
    visited = []
    while to_visit:
        node = to_visit.pop()
        visited.append(node)
        for v in graph[node]:
            if v not in visited + to_visit:
                to_visit.append(v)
    return visited

