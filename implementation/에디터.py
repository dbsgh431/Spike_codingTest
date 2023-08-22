import sys

input_string = sys.stdin.readline().rstrip()

left_stack = list(input_string)
right_stack = []

m = int(input())

cursor_index = len(input_string)
for i in range(m):
    input_order = sys.stdin.readline().rstrip()

    if input_order == 'L':
        if len(left_stack) > 0:
            pop = left_stack.pop()
            right_stack.append(pop)

    elif input_order == 'D':
        if  len(right_stack) > 0:
            pop = right_stack.pop()
            left_stack.append(pop)

    elif input_order == 'B':
        if len(left_stack) > 0:
            left_stack.pop()

    else:
        left_stack.append(input_order.split(" ")[1])

result = "".join(left_stack) + "".join(reversed(right_stack))

print(result)

"""import sys

input_string = list(sys.stdin.readline().rstrip())

m = int(input())

cursor_index = len(input_string)
for i in range(m):
    input_order = sys.stdin.readline().rstrip()

    if input_order == 'L' and cursor_index > 0:
        cursor_index -= 1
    elif input_order == 'D' and cursor_index < len(input_string):
        cursor_index += 1
    elif input_order == 'B' and cursor_index > 0:
        input_string.pop(cursor_index - 1)
        cursor_index -= 1
    elif input_order.split()[0] == 'P':
        input_string.insert(cursor_index, input_order.split()[1])
        cursor_index += 1
    else:
        pass

print("".join(input_string))
"""