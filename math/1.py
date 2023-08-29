import sys

while True:
    try:
        input_number = sys.stdin.readline().rstrip()
        start = len(input_number)
        i = 1
        while True:
            target = int("1" * i)
            if target % int(input_number) == 0:
                print(len(str(target)))
                break
            i += 1
    except:
        break


