import sys; sys.stdin = open('1227미로2_input.txt')


# def bfs(v, w):
#     visited[v][w] = 1
#
#     Q = []
#     Q.append((v, w))
#
#     while Q:
#         i, j = Q.pop(0)
#
#         if maze[i][j] == 3:
#             return 1
#
#         di = [0, 1, 0, -1]
#         dj = [1, 0, -1, 0]
#
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#
#             if (0 <= ni < N and 0 <= nj < N) and (maze[ni][nj] == 0 or maze[ni][nj] == 3) and visited[ni][nj] == 0:
#                 Q.append((ni, nj))
#                 visited[ni][nj] = visited[i][j] + 1
#
#     return 0
#
#
# T = 10
# N = 100
#
# for tc in range(1, T+1):
#     no = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]
#
#     visited = [[0] * (N+1) for _ in range(N)]
#
#     a = b = 0
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 a = i
#                 b = j
#
#     ans = bfs(a, b)
#
#     print(f'#{tc} {ans}')

def bfs(v, w):
    global flag

    visited[v][w] = 1

    Q = []
    Q.append((v, w))

    while Q:
        i, j = Q.pop(0)

        if maze[i][j] == 3:
            return flag

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and (maze[ni][nj] == 0 or maze[ni][nj] == 3) and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    flag = 0
    return flag


T = 10
N = 100

for tc in range(1, T+1):
    no = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    a = b = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                a = i
                b = j

    flag = 1
    bfs(a, b)

    print(f'#{tc} {flag}')