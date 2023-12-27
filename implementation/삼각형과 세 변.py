while True:
    try:
        a, b, c = map(int, input().split(" "))

        if a + b + c == 0:
            exit()

        m = max(a, b, c)

        s = sorted([a, b, c])

        if m >= s[1] + s[0]:
            print("Invalid")

        elif a == b == c:
            print("Equilateral")

        elif a != b and b != c and a != c:
            print("Scalene")

        elif a == b != c or a != b == c or b != c == a:
            print("Isosceles")
    except:
        exit()
        pass
