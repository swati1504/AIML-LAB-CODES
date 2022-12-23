V = 4
start2 = 0
path = []
visited = [False, False, False, False]
def tsp(graph,start):
    path.append(start)
    visited[start] = True
    min1 = 10000
    mini = 0
    flag = 0
    for i in range(0,V):
        if visited[i]==False and i!=start: 
            if min1 > graph[start][i]:
                min1 = graph[start][i]
                mini = i
                flag = 1
    if flag == 1:
        return tsp(graph,mini)
    else:
        path.append(start2)
        return path

graph2 = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
print(tsp(graph2,start2))






