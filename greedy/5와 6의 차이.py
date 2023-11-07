a, b = input().split(" ")

# 1. 최소: 모든 6 -> 5
min_a = int("".join(str(a).replace("6", "5")))
min_b = int("".join(str(b).replace("6", "5")))

min = min_a + min_b

# 2.최대 모든 5-> 6
max_a = int("".join(str(a).replace("5", "6")))
max_b = int("".join(str(b).replace("5", "6")))
max = max_a + max_b

print(min, max)
