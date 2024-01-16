import copy
from collections import deque

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if modi_arr[i][j] == 2 and visited[i][j] == 0:

                Q = deque()
                visited[i][j] = 1
                Q.append((i, j))

                while Q:
                    ci, cj = Q.popleft()

                    for di, dj in direct:
                        ni = ci + di
                        nj = cj + dj

                        if 0 <= ni < N and 0 <= nj < M:
                            if modi_arr[ni][nj] == 0 and visited[ni][nj] == 0:
                                Q.append((ni, nj))
                                visited[ni][nj] = visited[ci][cj] + 1
                                modi_arr[ni][nj] = 2

    this_safe = 0

    for i in range(N):
        for j in range(M):
            if modi_arr[i][j] == 0:
                this_safe += 1

    return this_safe


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
modi_arr = copy.deepcopy(arr)

cnt = 0
max_safe = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt += 1
            modi_arr[i][j] = 1
        for k in range(i, N):
            for m in range(j+1, M):
                if arr[k][m] == 0:
                    cnt += 1
                    modi_arr[k][m] = 1
                for n in range(k, N):
                    for l in range(m+1, M):
                        if arr[n][l] == 0:
                            cnt += 1
                            modi_arr[k][m] = 1
                        if cnt == 3:
                            this_cnt = bfs()
                            max_safe = max(max_safe, this_cnt)
                            modi_arr = copy.deepcopy(arr)

print(max_safe)
