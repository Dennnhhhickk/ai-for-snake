import os

def Road (body, height, width, x, y):
    dp = []
    p = []
    for i in range(width + 7):
        dp.append([])
        p.append([])
        for j in range(height + 7):
            dp[i].append(10000)
            p[i].append(0)
    q = []
    def do(temp, next_temp, tp):
        if (dp[next_temp[0]][next_temp[1]] == 10000) or (dp[next_temp[0]][next_temp[1]] < 0 and -dp[next_temp[0]][next_temp[1]] < dp[temp[0]][temp[1]] + 1):
            q.append(next_temp)
            dp[next_temp[0]][next_temp[1]] = dp[temp[0]][temp[1]] + 1
            p[next_temp[0]][next_temp[1]] = tp
    temp = [body[-1][0], body[-1][1]]
    for i in range(len(body)):
        dp[body[i][0]][body[i][1]] = -i - 1
    dp[temp[0]][temp[1]] = 0
    q.append(temp)
    #print(len(q))
    z = 0
    for temp in q:
        if (temp[0] + 1 < width):
            next_temp = [temp[0] + 1, temp[1]]
            do(temp, next_temp, 0)
        if (temp[0] > 0):
            next_temp = [temp[0] - 1, temp[1]]
            do(temp, next_temp, 1)
        if (temp[1] + 1 < height):
            next_temp = [temp[0], temp[1] + 1]
            do(temp, next_temp, 2)
        if (temp[1] > 0):
            next_temp = [temp[0], temp[1] - 1]
            do(temp, next_temp, 3)
        z += 1
    #print(z)
    now = [x, y]
    S = []
    temp = [body[-1][0], body[-1][1]]
    if (not(dp[x][y] == 10000)):
        while (not(now == temp)):
            #print(x, y)
            if (x < 0 or y < 0):
                quit(0)
            if (p[x][y] == 0):
                S.insert(0, 'RIGHT')
                x = x - 1
            elif (p[x][y] == 1):
                S.insert(0, 'LEFT')
                x = x + 1
            elif (p[x][y] == 2):
                S.insert(0, 'BOT')
                y = y - 1
            elif (p[x][y] == 3):
                S.insert(0, 'TOP')
                y = y + 1
            now = [x, y]
            #print(now, temp)
    #print(S)
    return S
