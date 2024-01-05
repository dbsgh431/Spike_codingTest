import sys

switch = int(sys.stdin.readline())


states = list(map(int, sys.stdin.readline().rstrip().split(" ")))

states.insert(0, 0)

student_count = int(sys.stdin.readline())
students = []

for i in range(student_count):
    students.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

for i in range(len(states)):
    if states[i] == 1:
        states[i] = True
    else:
        states[i] = False

for student in students:
    if student[0] == 1:
        for s in range(1, len(states)):
            if s % student[1] == 0:
                states[s] = not states[s]
    else:
        states[student[1]] = not states[student[1]]
        start, end = student[1] - 1, student[1] + 1
        while True:
            if start <= 0 or end >= len(states):
                break

            if states[start] == states[end]:
                states[start], states[end] = not states[start], not states[end]
                start, end = start - 1, end + 1
            else:
                break

for i in range(1, len(states)):
    if states[i]:
        states[i] = 1
    else:
        states[i] = 0

for i in range(1, len(states)):
    if i % 20 == 0:
        print()

    print(states[i], end=" ")
