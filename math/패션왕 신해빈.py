import sys
from collections import defaultdict

n = int(input())

for _ in range(n):
    # 의상 카테고리 별로 분류 하기위한 리스트를 디폴트로 가지는 딕셔너리
    closet = defaultdict(list)
    # 의상 종류
    num = int(input())
    # 경우의 수 계산을 위한 변수 cnt
    cnt = 1

    # 카테고리별 딕셔너리 저장
    for i in range(num):
        clothes, category = sys.stdin.readline().rstrip().split()
        closet[category].append(clothes)

    # 모든 경우의 수를 cnt에 누적
    for key in closet.keys():
        cnt *= (len(closet[key]) + 1)

    # 전체 경우의 수 - 1 => 하나의 의상이라도 입는 경우
    result = cnt - 1

    print(result)