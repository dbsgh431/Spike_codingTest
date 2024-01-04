n, new_score, p = map(int, input().split())

# 1. n이 0이면, 어떤 점수를 받더라도 1등이므로 1을 출력한다.
if n == 0:
    print(1)
    exit()
else:
    score = list(map(int, input().split()))

# 2. 입력한 점수의 개수가 p보다 작으면 순위에 올라갈 수 있으므로 새로운 점수를 추가한다.
if len(score) < p:
    score.append(new_score)
else:
    # 3. 입력한 점수의 개수가 p와 같으면, 새로운 점수가 기존 점수의 최솟값보다 큰 경우에만 추가할 수 있다.
    if min(score) >= new_score:
        print(-1)
        exit()
    else:
        score.remove(min(score))
        score.append(new_score)

# 4. 최종적으로 p개 이하의 점수 집합에 대해 내림차순으로 정렬 후 입력한 새로운 점수의 인덱스 + 1(인덱스는 0부터 시작하므로)가 해당 점수의 등수가 된다.
score.sort(reverse=True)
print(score.index(new_score) + 1)
