import math

h, w, n, m = map(int, input().split())
rows = math.ceil(h / (n + 1))
cols = math.ceil(w / (m + 1))
print(rows * cols)
