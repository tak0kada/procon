#inputs
mx, my = map(int, input().split())
sx, sy= map(int, input().split()); sx -= 1; sy -= 1
gx, gy = map(int, input().split()); gx -= 1; gy -= 1
M = [input() for i in range(mx)]

#buffer
B = [[0 for i in range(my)] for j in range(mx)]
Pre = [(sx, sy)]
Pos = []

step = 0 #constructs the answer
while (gx, gy) not in Pre:
    for prex, prey in Pre:
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if M[prex+i][prey+j] == '.' and B[prex+i][prey+j] == 0:
                Pos.append((prex+i, prey+j))
                B[prex+i][prey+j] = step
    Pre, Pos = Pos, []
    step += 1

print(step)
