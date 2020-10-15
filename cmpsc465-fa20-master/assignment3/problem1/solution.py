from collections import defaultdict

def transpose(graph,n):
    new_graph = defaultdict(list)
    for a in range(1,n+1):
        for b in graph[a]:
            new_graph[b].append(a)
    return new_graph

def dfs(graph,a,visit,stack):
    visit[a] = 1
    for b in graph[a]:
        if visit[b] == False:
            dfs(graph,b,visit,stack)
    stack.append(a)

def rdfs(graph,a,visit):
    visit[a] = 1
    for b in graph[a]:
        if visit[b] == False:
            rdfs(graph,b,visit)

def count(graph,n):
    stack = []
    visit = [False]*(n+1)
    for i in range(1,n+1):
        if visit[i] == False:
            dfs(graph,i,visit,stack)
    reverse_graph = transpose(graph,n)

    visit = [False]*(n+1)
    count = 0
    while len(stack) != 0:
        top = stack.pop()
        if visit[top] == False:
            count += 1
            rdfs(reverse_graph,top,visit)
    return count

n,m = list(map(int,input().split()))
graph = defaultdict(list)
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)

print(count(graph,n))