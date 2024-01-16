import sys
from collections import Counter

n, m = map(int, input().split())

dictionary = dict()
words = []
for i in range(n):
    word = sys.stdin.readline().rstrip()
    # 1. 입력 단어의 길이가 M이상인 단어만 저장한다.
    if len(word) >= m:
        #3.0 빈도수 계산을 위해 리스트 사용
        words.append(word)
        # 2. 단어 길이와 단어를 딕셔너리를 통해 저장한다.
        dictionary[word] = [0, len(word), word]

#3. 각 단어 별 빈도 수를 계산한다.
counter = Counter(words)

#4. 딕셔너리에 계산한 단어 별 빈도수를 추가하고 정렬 함수를 통해 정렬 기준을 모두 적용한다.
for key, value in zip(counter.keys(), counter.values()):
    dictionary[key][0] = value

result = sorted(dictionary.values(), key=lambda x: (-x[0], -x[1], x[2]))

for i in range(len(result)):
    print(result[i][2])
