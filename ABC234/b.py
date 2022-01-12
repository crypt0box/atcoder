import math

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
ans = 0

for i in range(N):
  for j in range(i+1,N):
    result = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
    ans = max(ans, result)

print(ans)