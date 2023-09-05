import sys

"""
    1. 자릿수가 바뀌는 경계는 9, 99, 999, ... 이다.
    2. 따라서 주어진 수 n과 경곗값과의 차이만큼 자릿수를 누적시켜 계산한다.
    
    // 다른 사람의 풀이
    0. 999가 n으로 주어졌을 때
    1. 1 ~ 9는 1자리, 10 ~ 99 는 2자리, 100 ~ 999는 3자리 이다.
    2. 따라서 1자리가 있는 수는 999개, 2자리가 있는 수는 990(10~999)개, 3자리가 있는 수는 900개(100~999) 이다.
    3. (999 - 1) + 1, (999 - 10) + 1, (999 -100) + 1, 와 같으므로 일반화하면 (n - i + 1)와 같으며 i를 10만큼씩 곱하면서 누적하여 계산한다. 
    
"""
n = sys.stdin.readline()

length = len(n) - 1

n = int(n)

result = 0
threshold = ""
while True:
    if n < 10:
        result += n
        print(result)
        break
    threshold = int("9" * (length - 1))

    x = n - threshold
    result += x * len(str(n))
    n = threshold
    length -= 1
