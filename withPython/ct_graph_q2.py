# 출처: 동빈나 (이코테 2021 강의 몰아보기) 3. DFS & BFS
# 미로 탈출
# 탈출을 위한 최소 칸의 개수 구하기

# => BFS

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]


from collections import deque

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))





                
            
